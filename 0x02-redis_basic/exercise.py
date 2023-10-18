#!/usr/bin
'''
Exercise Module
'''
import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''counts method call'''
    key = method.__qualname__
    
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
