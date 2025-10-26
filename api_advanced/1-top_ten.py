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
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "MyRedditApp/0.1"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])

            if posts:
                for post in posts:
                    title = post.get("data", {}).get("title")
                    print(title)
            else:
                print("None")
        else:
            print("None")

    except Exception:
        print("None")
