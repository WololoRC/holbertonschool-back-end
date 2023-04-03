#!/usr/bin/python3
"""Gather data from JSONPlacehole with input"""
import requests
from sys import argv


if __name__ == "__main__":
    a_out = []
    a_state = []

    r_name = requests.get(
            f'https://jsonplaceholder.typicode.com/users?id={argv[1]}')
    r_todos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")

    for record in r_todos.json():
        a_out.append(record.get('title'))
        a_state.append(record.get('completed'))

    u = r_name.json()[0].get('username')

    with open(f"{argv[1]}.CSV", 'w', encoding="utf-8") as a_file:
        for done in zip(a_out, a_state):
            a_file.write(
                    '"{}","{}","{}","{}"\n'.format(argv[1], u, done[1], done[0]))
