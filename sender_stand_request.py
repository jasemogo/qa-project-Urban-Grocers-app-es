import configuration
import requests
import data

# function to POST a new user
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)

# function to POST a new kit on a user
def post_new_kit(body, headers):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=body, headers=headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)