from functools import wraps
from time import sleep


def delay(a):
    @wraps(a)
    def wrapped():
        sleep(4)
        return a()
    return wrapped