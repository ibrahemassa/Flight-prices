import requests
import os

def post_new_row(first_name, last_name, email):

    headers = {
        "Authorization": "Bearer asdgyuias667t68",
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url="https://api.sheety.co/a2ccf90bd6fe726e5b3e13a9cd5d9f3b/flightDeals/users", headers=headers, json=body)
    response.raise_for_status()
    print(response.text)