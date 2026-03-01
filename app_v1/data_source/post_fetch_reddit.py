from pydantic import BaseModel, Field
from typing import List, Optional

from app_v1.data_source.data_source_base_class import DataSourceConfig, DataSourceBaseClass
from app_v1.config.config_loader import fetch_key_value
from app_v1.config.config_keys import RedditConfigKeys
import praw


class RedditFetchConfig(DataSourceConfig):
    """
    Configs related to post fetching from reddit
    Attributes:
        client_id:
        client_secret:
        user_agent:
    """
    client_id: str = Field(repr = False)
    client_secret: str = Field(repr = False)
    user_agent: str = Field(repr = False)
    user_name: Optional[str] = Field(repr = False)
    password: Optional[str] = Field(repr = False)
    target_subreddits: List[str]




class RedditPostFetch(DataSourceBaseClass):
    def __init__(self):
        config = RedditFetchConfig(
            client_id=fetch_key_value(RedditConfigKeys.CLIENT_ID),
            client_secret=fetch_key_value(RedditConfigKeys.CLIENT_SECRET),
            user_agent=fetch_key_value(RedditConfigKeys.USER_AGENT)
        )
        super().__init__(config)

        self.reddit_client = praw.Reddit(
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = config.user_agent
        )


    def fetch_post(self):
        pass


    def fetch_and_process_all_from_subreddit(self, subreddit_name:str):
        pass
