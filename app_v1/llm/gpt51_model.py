from app_v1.llm.llm_model import LLMModel
from app_v1.exceptions.llm_model_exceptions import APIKeyException


class GPT51Model(LLMModel):

    def __init__(self):
        self.temperature: int = 0
        self.model_name = "gpt-5.1"
        self.time_out: int = 30

    def initialize_model(self):
        api_key = ""
        if not api_key:
            raise APIKeyException("open")

    def get_post_classification_template(self) -> str:
        return """"""

    def get_model_name(self) ->str:
        return self.model_name
