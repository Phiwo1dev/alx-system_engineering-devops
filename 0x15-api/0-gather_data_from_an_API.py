#!/usr/bin/python3
"""
Returns to-do list info for a given employee.
"""

import requests
import sys


if __name__ == "__main__":
    # base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee info using the given employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter and count completed tasks.
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee name and the number of tasks completed.
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks.
    [print("\t {}".format(complete)) for complete in completed]
