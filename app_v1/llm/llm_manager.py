from app_v1.llm.llm_model import LLMModel

class LLMManager:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LLMManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._classification_model = None

        return cls._instance


    def set_classification_model(self, model:LLMModel):
        self._classification_model:LLMModel = model


    def get_classification_model(self) -> LLMModel:
        if self._classification_model is None:
            raise ValueError("classification_model is not set")
        return self._classification_model