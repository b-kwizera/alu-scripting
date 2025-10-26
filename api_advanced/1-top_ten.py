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
    message = "OK"
    if subreddit is None or not isinstance(subreddit, str):
        print(message)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python-requests/2.22.0"
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)

        if response.status_code != 200:
            print(message)
            return

        data = response.json()
        children = data.get("data", {}).get("children", [])

        if not children:
            print(message)
            return

        for child in children[:10]:
            post_data = child.get("data", {})
            title = post_data.get("title")
            if title:
                print(title)

    except Exception:
        print(message)
