#!/usr/bin/python3
"""
module queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API"""
    headers = {
        "User-Agent": "0x16. API_advanced-lilprof01"
        }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    sub = response.json().get("data").get("subscribers")
    return sub
