
class LLMModelException(Exception):
    """Base class for all LLM model related exceptions"""
    pass


class APIKeyException(LLMModelException):
    pass