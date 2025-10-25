ve function that returns a list of all hot article titles
for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
        """Recursively fetches all hot posts titles from a subreddit.

            Args:
                        subreddit (str): Subreddit to query.
                                hot_list (list, optional): Accumulated list of titles. Defaults to None.
                                        after (str, optional): Reddit pagination token. Defaults to None.

                                            Returns:
                                                        list or None: List of titles or None if subreddit is invalid.
                                                            """
                                                                if hot_list is None:
                                                                        hot_list = []

                                                                            url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                                                                                headers = {"User-Agent": "alu-scripting/1.0"}
                                                                                    params = {"limit": 100, "after": after}

                                                                                        try:
                                                                                                response = requests.get(url, headers=headers, params=params, allow_redirects=False)
                                                                                                        if response.status_code != 200:
                                                                                                                    return None

                                                                                                                            data = response.json().get("data", {})
                                                                                                                                    children = data.get("children", [])

                                                                                                                                            for post in children:
                                                                                                                                                        title = post.get("data", {}).get("title")
                                                                                                                                                                    if title:
                                                                                                                                                                                    hot_list.append(title)

                                                                                                                                                                                            after = data.get("after")
                                                                                                                                                                                                    if after is None:
                                                                                                                                                                                                                return hot_list

                                                                                                                                                                                                                        # Recursive call for the next page
                                                                                                                                                                                                                                return recurse(subreddit, hot_list, after)

                                                                                                                                                                                                                                    except Exception:
                                                                                                                                                                                                                                            return None

