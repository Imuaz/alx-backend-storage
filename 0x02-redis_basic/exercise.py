#!/usr/bin/env python3
'''
Exercise Module
'''
import redis
from uuid import uuid4
from typing import Callable, Optional, Union


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
        
