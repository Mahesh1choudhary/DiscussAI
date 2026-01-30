from pydantic import BaseSettings

class GPT51SecretSchema(BaseSettings):
    api_key: str