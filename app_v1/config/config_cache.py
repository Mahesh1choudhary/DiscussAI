from cachetools import TTLCache
import threading

from app.config.config_keys import ConfigCacheConfigKeys
from app.config.config_loader import fetch_key_value

cache_lock = threading.Lock()
cache = TTLCache(maxsize= float(ConfigCacheConfigKeys.MAX_SIZE), ttl = float(ConfigCacheConfigKeys.TTL_SECONDS))


def get_key(key: str):
    value = cache.get(key)
    if value is None:
        with cache_lock:
            value = fetch_key_value(key)
            set_key(key, value)
    return value


def set_key(key, value):
    cache[key] = value
