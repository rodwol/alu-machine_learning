#!/usr/bin/env python3
"""
Fetches and prints the location of a GitHub user using the GitHub API.
"""

import sys
import requests
from datetime import datetime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API user URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)

    # Handle rate limit
    if response.status_code == 403:
        reset_time = response.headers.get("X-RateLimit-Reset")
        if reset_time:
            reset_timestamp = int(reset_time)
            current_time = int(datetime.now().timestamp())
            minutes_left = int((reset_timestamp - current_time) / 60)
            print(f"Reset in {minutes_left} min")
        else:
            print("Rate limit exceeded.")
        sys.exit(0)

    # Handle user not found
    if response.status_code == 404:
        print("Not found")
        sys.exit(0)

    # Handle successful response
    if response.status_code == 200:
        user_data = response.json()
        location = user_data.get("location")
        if location:
            print(location)
        else:
            print("No location found")
    else:
        print("Error:", response.status_code)
