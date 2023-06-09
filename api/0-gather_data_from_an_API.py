#!/usr/bin/python3
"""Gather data from JSONPlacehole with input"""
import requests
from sys import argv


if __name__ == "__main__":
    a_out = []

    # @do: done #
    do = 0
    # @un: undone #
    un = 0

    r_name = requests.get(
            f"https://jsonplaceholder.typicode.com/users?id={argv[1]}")
    r_todos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")

    for record in r_todos.json():
        if record.get('completed') is True:
            a_out.append(record.get('title'))
            do = do + 1

        else:
            un = un + 1

    if do == 0:
        quit()

    print("Employee {}".format(r_name.json()[0].get('name')), end="")
    print(" is done with tasks({}/{}):".format(do, do + un))
    for done in a_out:
        print("\t {}".format(done))
