#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    all_users = get(users_url).json()

    all_dict = {}
    for user in all_users:
        task_list = []

        main_url = "https://jsonplaceholder.typicode.com"
        task_url = main_url + "/user/{}/todos".format(user.get("id"))
        name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user.get("id"))

        all_task = get(task_url).json()
        all_name = get(name_url).json()
        for task in all_task:
            task_dict = {}
            task_dict.update({"username": all_name.get("username"),
                              "task": task.get("title"),
                              "completed": task.get("completed")})
            task_list.append(task_dict)

        all_dict.update({user.get("id"): task_list})

    with open("todo_all_employees.json", 'w') as f:
        dump(all_dict, f)
