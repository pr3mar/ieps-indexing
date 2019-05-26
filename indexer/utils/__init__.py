# contains util functions as timer, etc
from functools import wraps
from datetime import datetime


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        # print(f'Time elapsed for `{f.__name__}`: {((datetime.now() - start).total_seconds() * 1e3):.2f} ms') # TODO: add logging with debug level
        return result
    return wrapper


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        # print(f'Time elapsed for `{f.__name__}`: {((datetime.now() - start).total_seconds() * 1e3):.2f} ms')
        msPassed = ((datetime.now() - start).total_seconds() * 1e3)
        return msPassed, result
    return wrapper
