#!/usr/bin/python3
""" Script to export data in the JSON format. """

import json
import requests as r
#import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = r.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    to_do = r.get(url + "todos", params={"user_id": user_id}).json()

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({user_id: [{"task": e.get("title"),
                              "completed": e.get("completed"),
                              "username": username} for e in to_do]},
                  jsonfile)
