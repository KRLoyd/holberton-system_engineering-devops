#!/usr/bin/python3
"""
Module for Task 0 of Holberton Project #314
"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers for a subreddit.

    Subreddit is passed as an argument.
    If the subreddit is not valid, 0 is returned.
    """
    # import json
    import requests
    import sys

    # set variables
    request_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent':
               'chrome:number_of_subscribers_function:v1 (by /u/remyjuke)'}

    response = requests.get(request_url,
                            headers=headers,
                            allow_redirects=False)

    response_code = response.status_code
    if (response_code >= 300):
        return 0

    subscriber_count = response.json().get("data").get("subscribers")
    return subscriber_count
