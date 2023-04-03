#!/usr/bin/python3
"""
Gather data from JSONPlacehole with input
and export it on a JSON file.

This script takes all the data from DB.
"""
import requests
import json


if __name__ == "__main__":
    cnt = 1
    my_dict = {}

    while True:
        # By iteration we take data from API #
        a_list = []
        r_name = requests.get(
                f'https://jsonplaceholder.typicode.com/users?id={cnt}')
        r_todos = requests.get(
                f"https://jsonplaceholder.typicode.com/todos?userId={cnt}")

        # If 'users?id={cnt}' is empty#
        if r_name.json() == []:
            break

        user = r_name.json()[0].get("username")

        for r in r_todos.json():
            safe_dict = dict(
                    username=user, task=r.get('title'),
                    completed=r.get('completed'))

            a_list.append(safe_dict)
            my_dict.update({f"{cnt}": a_list})

        cnt = cnt + 1

    with open("todo_all_employees.json", 'w', encoding='utf-8') as a_json:
        json.dump(my_dict, a_json)
