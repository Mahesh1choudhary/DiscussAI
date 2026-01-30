from pydantic import BaseConfig, Field


class GPT51ConfigSchema(BaseConfig):
    temperature: float = Field(ge=0.0, le=2.0)
    timeout: int = Field(ge=0)


class ConfigCacheConfigSchema(BaseConfig):
    max_size: int = Field(ge=0)
    ttl_seconds: int = Field(ge=0)
