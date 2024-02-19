#!/usr/bin/python3
"""Exports to-do list info for employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Get the user ID from the command-line arguments.
    user_id = sys.argv[1]

    # defines the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user info from the API and
    #   convert the response into a JSON file
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extracts the username from user data
    username = user.get("username")

    # Fetch the to-do list items for the
    #   given user ID and convert the output into a JSON file
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write each item's details (user ID  as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
