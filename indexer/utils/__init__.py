# contains util functions as timer, etc
from functools import wraps
from datetime import datetime


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = f(*args, **kwargs)
        print(f'Time elapsed for `{f.__name__}`: {(datetime.now() - start).total_seconds() * 1e3} ms')
        return result
    return wrapper
