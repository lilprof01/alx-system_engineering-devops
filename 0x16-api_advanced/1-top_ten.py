#!/usr/bin/python3
"""
module queries the Reddit API and prints the titles of the top 10
hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """function prints titles of the top 10 hot posts"""
    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    response_ = response.json().get("data")
    for child in response_.get("children"):
        print(child.get("data").get("title"))
