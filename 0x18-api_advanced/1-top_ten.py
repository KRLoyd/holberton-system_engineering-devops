#!/usr/bin/python3
"""
Module for Task 1 of Holberton School Project 314
"""


def top_ten(subreddit):
    """
    Function to print the titles of the first 10 hot posts of a subreddit.

    Subreddit is provided as a parameter.
    If an invalid subreddit is supplied, "None" is printed
    """

    import requests
    import sys

    # Set vairables
    request_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'chrome:top_ten_function:v1 (by /u/remyjuke)'}

    response = requests.get(request_url,
                            headers=headers,
                            allow_redirects=False)

    response_code = response.status_code
    if (response_code >= 300):
        print("None")
        return

    post_list = response.json().get("data").get("children")

    for i in range(0, 10):
        print(post_list[i].get("data").get("title"))
