from abc import ABC, abstractmethod
from typing import Dict, Any

from pydantic import BaseModel, Field
from dataclasses import dataclass



@dataclass(frozen=True)
class Post:
    """
    Object representing a post

    Attributes:
        post_id: Unique identifier of the post.
        post_source: origin of the post- reddit, leetcode, etc
        post_source_id: post id in the source of origin
        post_data: Raw post payload as returned by the source.
    """
    post_id: str
    post_source: str
    post_source_id: str
    post_data: Dict[str, Any]

    def __post_init__(self):
        """ post basic validation"""
        if not self.post_id:
            raise ValueError("post_id cannot be empty")


class FetchConfig(BaseModel):
    """Base class for all fetch configs"""
    pass


class PostFetchBaseClass(ABC):
    """Base class for post fetching classes """
    def __init__(self, config: FetchConfig):
        self.config = config

    @abstractmethod
    def fetch_post(self, post_source_id:str):
        """

        :param post_source_id: unique identifier for a post in the source
        :return:
        """
        pass



class LeetCodePostFetch(PostFetchBaseClass):
    def __init__(self):
        # TODO: add leetcode configs accordingly
        super().__init__(FetchConfig())


