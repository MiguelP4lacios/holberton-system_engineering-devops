#!/usr/bin/python3
"""Module API """

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given
    subreddit."""

    lists = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"

    if after:
        urls = url.format(subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    header = {"User-Agent": "RED"}

    request = requests.get(url, headers=header)

    if request.status_code != 200:
        return None

    if request.status_code == 200:
        children = request.json().get("data").get("children")
        after = request.json().get("data").get("after")

        if children is None:
            return None

        for child in children:
            tittles = child.get("data").get("title")
            hot_list.append(tittles)

    if after:
        recurse("{}".format(subreddit), after=after)
    return hot_list
