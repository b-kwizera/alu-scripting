#!/usr/bin/python3
"""Recursive function that queries the Reddit API, parses hot article titles,
and prints a sorted count of given keywords (case-insensitive)."""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
        """Recursively counts occurrences of keywords in subreddit hot posts."""
            if after is None:
                        counts = {}

                            url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                                headers = {"User-Agent": "Mozilla/5.0"}
                                    params = {"limit": 100, "after": after}
                                        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

                                            # Stop if invalid subreddit
                                                if response.status_code != 200:
                                                            return

                                                            data = response.json().get("data", {})
                                                                posts = data.get("children", [])

                                                                    # Normalize word list and count words
                                                                        for post in posts:
                                                                                    title_words = post["data"]["title"].lower().split()
                                                                                            for word in word_list:
                                                                                                            word_lower = word.lower()
                                                                                                                        counts[word_lower] = counts.get(word_lower, 0) + title_words.count(word_lower)

                                                                                                                            # Continue recursively if there's another page
                                                                                                                                after = data.get("after")
                                                                                                                                    if after:
                                                                                                                                                return count_words(subreddit, word_list, after, counts)
                                                                                                                                                else:
                                                                                                                                                            # Sort results by count (desc) then alphabetically
                                                                                                                                                                    sorted_counts = sorted(
                                                                                                                                                                                        [(word, count) for word, count in counts.items() if count > 0],
                                                                                                                                                                                                    key=lambda x: (-x[1], x[0])
                                                                                                                                                                                                            )
                                                                                                                                                                            for word, count in sorted_counts:
                                                                                                                                                                                            print(f"{word}: {count}")
                                                                                                                                                              #!/usr/bin/python3
                                                                                                                                                              """Recursive function that queries the Reddit API, parses hot article titles,
                                                                                                                                                              and prints a sorted count of given keywords (case-insensitive)."""

                                                                                                                                                              import requests


                                                                                                                                                              def count_words(subreddit, word_list, after=None, counts={}):
                                                                                                                                                                      """Recursively counts occurrences of keywords in subreddit hot posts."""
                                                                                                                                                                          if after is None:
                                                                                                                                                                                      counts = {}

                                                                                                                                                                                          url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                                                                                                                                                                                              headers = {"User-Agent": "Mozilla/5.0"}
                                                                                                                                                                                                  params = {"limit": 100, "after": after}
                                                                                                                                                                                                      response = requests.get(url, headers=headers, params=params, allow_redirects=False)

                                                                                                                                                                                                          # Stop if invalid subreddit
                                                                                                                                                                                                              if response.status_code != 200:
                                                                                                                                                                                                                          return

                                                                                                                                                                                                                          data = response.json().get("data", {})
                                                                                                                                                                                                                              posts = data.get("children", [])

                                                                                                                                                                                                                                  # Normalize word list and count words
                                                                                                                                                                                                                                      for post in posts:
                                                                                                                                                                                                                                                  title_words = post["data"]["title"].lower().split()
                                                                                                                                                                                                                                                          for word in word_list:
                                                                                                                                                                                                                                                                          word_lower = word.lower()
                                                                                                                                                                                                                                                                                      counts[word_lower] = counts.get(word_lower, 0) + title_words.count(word_lower)

                                                                                                                                                                                                                                                                                          # Continue recursively if there's another page
                                                                                                                                                                                                                                                                                              after = data.get("after")
                                                                                                                                                                                                                                                                                                  if after:
                                                                                                                                                                                                                                                                                                              return count_words(subreddit, word_list, after, counts)
                                                                                                                                                                                                                                                                                                              else:
                                                                                                                                                                                                                                                                                                                          # Sort results by count (desc) then alphabetically
                                                                                                                                                                                                                                                                                                                                  sorted_counts = sorted(
                                                                                                                                                                                                                                                                                                                                                      [(word, count) for word, count in counts.items() if count > 0],
                                                                                                                                                                                                                                                                                                                                                                  key=lambda x: (-x[1], x[0])
                                                                                                                                                                                                                                                                                                                                                                          )
                                                                                                                                                                                                                                                                                                                                          for word, count in sorted_counts:
                                                                                                                                                                                                                                                                                                                                                          print(f"{word}: {count}")

