#!/usr/bin/env python3
"""
Create a web cache using Redis.
"""
import redis
import requests


class WebCache:
    def __init__(self):
        self.redis = redis.Redis()

    def get_page(self, url: str) -> str:
        """Get a page and cache its value, or retrieve the cached content.

        Args:
            url (str): The URL of the web page to fetch.

        Returns:
            str: The content of the web page.
        """
        cached_key = f"cached:{url}"
        count_key = f"count:{url}"

        cached_value = self.redis.get(cached_key)

        if cached_value is not None:
            # If the value is cached, increment the count and return the cached
            self.redis.incr(count_key)
            self.redis.setex(cached_key, 10, cached_value)
            return cached_value.decode("utf-8")

        # If not cached, fetch the page, cache it, and increment the count
        response = requests.get(url)
        self.redis.incr(count_key)
        self.redis.setex(cached_key, 10, response.text)
        return response.text


if __name__ == "__main__":
    web_cache = WebCache()
    cached_page = web_cache.get_page('http://slowwly.robertomurray.co.uk')
    print(cached_page)
