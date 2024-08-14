#!/usr/bin/python3
"""
Script to print the titles of the top 10 hot posts on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; RedditAPI/0.1)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            results = response.json().get("data")
            if results:
                for post in results.get("children", []):
                    print(post.get("data", {}).get("title"))
            else:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")