from abc import ABC, abstractmethod


class LLMModel(ABC):
    """
    Abstract class for LLM models. To give freedom of model changes and prompt changes within models
    """

    @abstractmethod
    def initialize_model(self) -> None:
        pass

    @abstractmethod
    def get_post_classification_template(self) -> str:
        pass
