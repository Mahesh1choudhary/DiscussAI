from cachetools import TTLCache

cache_lock = threading.Lock()
cache = TTLCache()