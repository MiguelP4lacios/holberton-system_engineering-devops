#!/usr/bin/python3
"""Module API
"""

import json
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""

    URL = "http://reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    headers = {'User-agent': 'graphic design'}
    request = requests.get(URL, headers={'User-agent': 'graphic design'})

    try:
        child = request.json().get("data").get("children")

        if child:
            for titles in child:
                print(titles.get("data").get("title"))
        else:
            print("None")
    except:
        print("None")
