import requests
import time
from typing import List, Dict

from app_v1.data_source.data_source_base_class import DataSourceConfig


class LeetcodeFetchConfig(DataSourceConfig):

    # auth
    leetcode_session:str = "session id "
    csrf_token:str = "token"

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



class LeetcodeClient:
    def __init__(self, config:LeetcodeFetchConfig):
        self.config = config

        self.session = requests.Session()


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



    def execute_query(self, query:str, variables:dict):
        headers = self._build_headers()
        response = self.session.post(
            self.config.base_url,
            json={
                "query": query,
                "variables": variables
            },
            headers=headers,
            timeout=self.config.timeout,
        )


        response.raise_for_status()
        return response.json()





if __name__ == "__main__":

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
    variables = {
        "topicId": "7595344"
    }

    client = LeetcodeClient(LeetcodeFetchConfig())
    client.execute_query(query=query, variables=variables)

    print(f"completed")
