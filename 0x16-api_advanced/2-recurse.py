#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import requests as r


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    """ Queries to Reddit API """
    headers = {
        "User-Agent": "Mozilla/5.0"
        }
    param = {
        "after": after
    }
    response = r.get(url, headers=headers, params=param, allow_redirects=False)
    if response.status_code == 404:
        print(None)
    else:
        posts = response.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = response.json().get("data").get("after")
        if after is not None:
                recurse(subreddit, hot_list, after)
        return hot_list
