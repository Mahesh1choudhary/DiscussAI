from abc import ABC, abstractmethod


class FetchConfig:
    pass

class PostFetchBaseClass(ABC):
    def __init__(self, config: FetchConfig):
        self.config = config

    @abstractmethod
    def fetch_post(self):
        pass



class LeetCodePostFetch(PostFetchBaseClass):
    def __init__self(self):
        # TODO: add leetcode configs accordingly
        super().__init__(FetchConfig())