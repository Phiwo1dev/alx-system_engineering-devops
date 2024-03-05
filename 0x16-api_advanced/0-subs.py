#!/usr/bin/python3
"""
This function queries the Reddit API and returns total number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API
    - returns 0, If not a valid subreddit.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
