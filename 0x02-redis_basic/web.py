#!/usr/bin/env python3
"""
web module
"""
import redis
import requests

rc = redis.Redis()


def get_page(url: str) -> str:
    """get a page and cache value"""

    # Check if the page is already cached.
    cached_page = rc.get(f"cached:{url}")
    if cached_page is not None:
        return cached_page

    # Fetch the page from the remote server.
    resp = requests.get(url)

    # Increment the hit counter for the page.
    rc.incr(f"count:{url}")

    # Cache the page for 10 seconds.
    rc.setex(f"cached:{url}", 10, resp.text)

    return resp.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
