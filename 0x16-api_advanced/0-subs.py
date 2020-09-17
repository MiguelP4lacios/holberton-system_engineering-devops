#!/usr/bin/python3
"""Module API
"""

import json
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and
    returns the number of subscribers
    """

    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-agent': 'RED'}
    res = requests.get(url=URL, headers=headers)
    try:
        return int(res.json().get('data').get('subscribers'))
    except:
        return 0
