import requests
import json
import os
import sys

randomuser_url = "https://randomuser.me/api"


def get_users(count):
    response = requests.get("{}?results={}".format(randomuser_url, count))
    return response


if __name__ == '__main__':
    '''Retrieve specified number of users and write to a file the users.  
        The actionType and top properties are also added, which are set to None.
        This file format is expected with the CensusToyService class ctor.
    '''
    num_users = int(input("Number of users: ").strip())
    file_name = input("File name: ").strip()

    response = get_users(num_users)
    if response.status_code != 200:
        raise Exception("Could not retrieve{} users, status code {}".format(
            num_users, response.status_code))
    users = response.json()['results']

# write  empty  action and top values, with the users to a file
    test_data_file = open(file_name, "w")
    test_data = {}
    test_data["actionType"] = None
    test_data["top"] = None
    test_data["users"] = users
    print(test_data)
    json.dump(test_data, test_data_file)
    test_data_file.close()
