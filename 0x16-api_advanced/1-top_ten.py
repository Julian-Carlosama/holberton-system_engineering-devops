#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import requests as r 


def top_ten(subreddit):
    """Print top 10 post given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    """ Queries to Reddit API """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    param = {
        "limit": 10
    }
    response = r.get(url, headers=headers, params=param, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return 
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results.get("children")]
