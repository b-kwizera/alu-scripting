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
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:subreddit.top.posts:v1.0.0 (by /u/testuser)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])

            if len(children) == 0:
                print(None)
                return

            for child in children:
                post_data = child.get("data", {})
                title = post_data.get("title", "")
                print(title)
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
    except (ValueError, KeyError):
        print(None)
