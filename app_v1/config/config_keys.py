from enum import IntEnum, Enum


class GPT51ConfigKeys(str, Enum):
    TEMPERATURE  = "TEMPERATURE"
    TIME_OUT = "TIME_OUT"

class ConfigCacheConfigKeys(IntEnum):
    MAX_SIZE = 1000
    TTL_SECONDS = 1000


class EnvironmentConfigKeys(str, Enum):
    ENV = "ENV"


class RedditConfigKeys(str, Enum):
    CLIENT_ID = "CLIENT_ID"
    CLIENT_SECRET = "CLIENT_SECRET"
    USER_AGENT = "USER_AGENT"