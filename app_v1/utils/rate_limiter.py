import functools
import inspect

def dynamic_rate_limit(func):
    def check_rate_limit(user_name:str):
        pass #TODO: add the appropriate logic later
    # will raise 429 error if limit exceeds
    # rate limit will be on window -> will keep daily basis for the starting phase
    # Limit will be different for each user- will store somewhere. Or can introduce tier based limit( can store user level for tier)

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        user_name = kwargs.get("user_name")
        if not user_name:
            raise RuntimeError(
                f"Function '{func.__name__}' is decorated with @dynamic_rate_limit "
                f"but was called without a 'user_name' argument."
            )

        check_rate_limit(user_name)
        return await func(*args, **kwargs)


    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        user_name = kwargs.get("user_name")
        if not user_name:
            raise RuntimeError(
                f"Function '{func.__name__}' is decorated with @dynamic_rate_limit "
                f"but was called without a 'user_name' argument."
            )

        check_rate_limit(user_name)
        return func(*args, **kwargs)


    if inspect.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper
