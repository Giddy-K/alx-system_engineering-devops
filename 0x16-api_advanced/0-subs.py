#!/usr/bin/python3
"""
Script that queries the number of subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a given subreddit.
    If the subreddit is invalid or does not exist, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; RedditAPI/0.1)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.RequestException:
        return 0

    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0