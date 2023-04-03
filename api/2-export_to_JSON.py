#!/usr/bin/python3
"""
Gather data from JSONPlacehole with input
and export it ona JSON file.
"""
from sys import argv
import json
import requests


if __name__ == "__main__":
    a_list = []
    my_dict = {f"{argv[1]}": a_list}

    r_name = requests.get(
            f'https://jsonplaceholder.typicode.com/users?id={argv[1]}')
    r_todos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")

    user = r_name.json()[0].get("username")

    for r in r_todos.json():
        safe_dict = dict(
                task=r.get(
                    "title"), completed=r.get("completed"), username=user)

        a_list.append(safe_dict)

    with open(f"{argv[1]}.json", 'w', encoding='utf-8') as a_json:
        json.dump(my_dict, a_json)
