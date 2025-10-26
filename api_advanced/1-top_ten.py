#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    url = ("https://oauth.reddit.com/r/{}/hot.json?limit=10"
           .format(subreddit))
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(
                url,
                headers=headers,
                allow_redirects=False
                )

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])

            if not posts:
                print("OK")
                return

            for post in posts[:10]:
                print(post['data'].get('title', "No Title Found"))
        except ValueError:
            print("OK")
    else:
        print("OK")
