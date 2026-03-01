from abc import ABC, abstractmethod
from typing import Dict, Any

from pydantic import BaseModel, Field
from dataclasses import dataclass


class DataSourceConfig(BaseModel):
    """Base class for all fetch configs"""
    pass


class DataSourceBaseClass(ABC):
    """Base class for data source classes """
    def __init__(self, config: DataSourceConfig):
        self.config = config

    @abstractmethod
    def fetch_post(self, post_source_id:str):
        """

        :param post_source_id: unique identifier for a post in the source
        :return:
        """
        pass



class LeetCodePostFetch(DataSourceBaseClass):
    def __init__(self):
        # TODO: add leetcode configs accordingly
        super().__init__(DataSourceConfig())


