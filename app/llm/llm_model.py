from abc import ABC, abstractmethod


class LLMModel(ABC):
    """
    Abstract class for LLM models. To give freedom of LLM and prompt changes for models
    """

    @abstractmethod
    def initialize_model(self, temperature: int = 0):
        pass

    @abstractmethod
    def get_post_classification_template(self):
        pass
