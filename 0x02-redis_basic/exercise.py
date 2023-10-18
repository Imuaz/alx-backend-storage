#!/usr/bin
'''
Exercise Module
'''
import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''ounts method calls.'''

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''invokes the original method'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def cache_decorator(method: Callable) -> Callable:
    '''add call history to a method'''
    key = method.__qualname__
    inputs, outputs = key + ":inputs", key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''logs inputs and outputs'''
        self._redis.rpush(inputs, str(args))
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(outputs, output)
        return output

    return wrapper

def replay(method: Callable) -> None:
    '''prints the history of method calls'''
    key = method.__qualname__
    count_key = key + ":count"
    inputs, outputs = key + ":inputs", key + ":outputs"
    redis_client = method.__self__._redis

    count = redis_client.get(count_key)
    if count:
        count = count.decode("utf-8")
        print(f"{key} was called {count} times:")
        input_list = redis_client.lrange(inputs, 0, -1)
        output_list = redis_client.lrange(outputs, 0, -1)
        IOTuple = zip(input_list, output_list)
        for inp, outp in list(IOTuple):
            attr, data = inp.decode("utf-8"), outp.decode("utf-8")
            print(f"{key}(*{attr}) -> {data}")
    else:
        print(f"{key} has not been called.")


class Cache:
    '''stores and retrieves data'''
    def __init__(self):
        '''Initialize the Chache'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def _generate_key() -> str:
        '''Generates a unique key for data storage'''
        return str(uuid4())

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores data in the cache and returns the key'''
        key = self._generate_key()
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        '''Retrieves data from cache by key and optionally applys
        transformation function'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    @staticmethod
    def get_str(data: str) -> str:
        '''Converts a string data stored in the cache to a string type'''
        return data.decode('utf-8')

    @staticmethod
    def get_int(data: str) -> int:
        '''Converts a string data stored in the cache to an integer type'''
        return int(data)
