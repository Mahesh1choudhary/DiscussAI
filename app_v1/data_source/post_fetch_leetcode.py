import asyncio

import httpx
import requests
import time
from typing import List, Dict,Any

from pydantic import BaseModel, Field

from app_v1.data_source.data_source_base_class import DataSourceConfig


class LeetcodeQueryTemplate(BaseModel):
    query:str
    variables:Dict[str, Any] = Field(default_factory=dict)

    def build_query(self, **kwargs) -> Dict[str, Any]:
        return {
            "query": self.query,
            "variables": {**self.variables, **kwargs},
        }

class LeetcodeFetchConfig(DataSourceConfig):

    # auth
    leetcode_session:str = ""
    csrf_token:str = ""

    #url
    base_url:str = "https://leetcode.com/graphql/"

    # retry settings
    timeout: int = 30
    max_retries: int = 3
    retry_backoff: int = 2

    # default headers
    user_agent:str = "Mozilla/5.0"
    origin:str = "https://leetcode.com"
    referer:str = "https://leetcode.com"

    # to avoid rate limiting
    request_delay:int = 2

    @property
    def generate_headers(self) -> Dict[str, str]:
        return {
            "content-type": "application/json",
            "user-agent": self.user_agent,
            "origin": self.origin,
            "referer": self.referer,
            "x-csrftoken": self.csrf_token,
            "cookie": f"csrftoken={self.csrf_token}; LEETCODE_SESSION={self.leetcode_session}",
        }

    GET_POST_BY_ID:LeetcodeQueryTemplate = LeetcodeQueryTemplate(
        query = """
                query discussPostDetail($topicId: ID!) {
                  ugcArticleDiscussionArticle(topicId: $topicId) {
                    title
                    content
                    tags {
                      name
                    }
                    createdAt
                  }
                }
                """
        ,
        variables={
            "topicId": "7595344"
        }
    )

    GET_LIST_OF_POSTS:LeetcodeQueryTemplate = LeetcodeQueryTemplate(
        query = """
            query discussPostItems($orderBy: ArticleOrderByEnum,$keywords: [String]!, $tagSlugs: [String!], $skip: Int, $first: Int) {
              ugcArticleDiscussionArticles(
                orderBy: $orderBy
                keywords: $keywords
                tagSlugs: $tagSlugs
                skip: $skip
                first: $first
              ) {
                pageInfo {
                  hasNextPage
                }
                edges {
                  node {
                    topicId
                    title
                    summary
                    createdAt
                    tags {
                      name
                    }
                  }
                }
              }
            }
            """
        ,
        variables={
            "orderBy": "MOST_RECENT", # we will fetch till a certain data in order
            "keywords": [""],
            "tagSlugs": ["interview"], # update if other posts are needed
            "skip": 0,
            "first": 50
        }
    )

class LeetcodeClient:
    def __init__(self, config:LeetcodeFetchConfig):
        self.config = config
        self.client = None

    async def __aenter__(self):
        self.client = httpx.AsyncClient(timeout=self.config.timeout)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.aclose()


    def _build_headers(self):
        cookie = f"csrftoken={self.config.csrf_token}; LEETCODE_SESSION={self.config.leetcode_session}"
        return {
            "content-type": "application/json",
            "user-agent": self.config.user_agent,
            "origin": self.config.origin,
            "referer": self.config.referer,
            "x-csrftoken": self.config.csrf_token,
            "cookie": cookie,
        }



    async def get_post_with_id(self, topic_id: str):
        headers = self._build_headers()

        response = await self.client.post(
            self.config.base_url,
            json=self.config.GET_POST_BY_ID.build_query(topicId=topic_id),
            headers=headers,
            timeout=self.config.timeout,
        )

        response.raise_for_status()
        return response.json()

    async def get_list_of_posts(self, skip:int, batch_size:int=20) -> List[str]:
        headers = self._build_headers()
        response = await self.client.post(
            self.config.base_url,
            json=self.config.GET_LIST_OF_POSTS.build_query(skip=skip, first=batch_size),
            headers=headers,
            timeout=self.config.timeout,
        )

        response.raise_for_status()
        data = response.json()
        post_data_list: List[Any] = data.get('data', {}).get('ugcArticleDiscussionArticles', {}).get('edges', [])

        topic_id_list = []
        for post_data in post_data_list:
            topic_id:str = post_data.get('node', {}).get('topicId', None)
            if topic_id is not None:
                topic_id_list.append(topic_id)

        return topic_id_list


