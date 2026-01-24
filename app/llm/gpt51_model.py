from app.llm.llm_model import LLMModel
from app.exceptions.llm_model_exceptions import APIKeyException


class GPT51Model(LLMModel):

    def __init__(self):
        temperature: int = 0
        model_name = "gpt-5.1"
        time_out: int = 30

    def initialize_model(self):
        api_key =
        if not api_key:
            raise APIkeyException("open")

    def get_post_classification_template(self):
        return
