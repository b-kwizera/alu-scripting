#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers."""

import requests


def number_of_subscribers(subreddit):
        """Return the number of subscribers for a given subreddit."""
            if subreddit is None or not isinstance(subreddit, str):
                        return 0

                        url = f"https://www.reddit.com/r/{subreddit}/about.json"
                            headers = {"User-Agent": "CustomUserAgent/1.0"}

                                try:
                                            response = requests.get(url, headers=headers, allow_redirects=False)
                                                    if response.status_code != 200:
                                                                    return 0
                                                                        data = response.json()
                                                                                return data.get("data", {}).get("subscribers", 0)
                                                                                except Exception:
                                                                                            return 0

