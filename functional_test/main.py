import requests
import json

URL = "http://localhost:8000"

def get(header, url, data):
    response = requests.get(url, headers=header, data=data)
    print(response.status_code)
    if hasattr(response, 'json'):
        print(response.json())
        return response.json()
    else:
        print(response.content)


def post(header, url, data):
    response = requests.post(url, headers=header, data=data)
    print(response.status_code)
    if hasattr(response, 'json'):
        print(response.json())
        return response.json()
    else:
        print(response.content)



if __name__ == "__main__":
    # register flow
    register_url = URL + "/users/auth/registration/"
    data = {
        "username": "test_2",
        "email": "test_2@exmaple.com",
        "password1": "Tdjsagdjhgasjd_123123",
        "password2": "Tdjsagdjhgasjd_123123"
    }
    headers = {
        "Content-Type": "application/json"
    }
    post(headers, register_url, json.dumps(data))
    # login flow
    login_url = URL + "/users/auth/login/"
    data = {
        "username": "test_2",
        "password": "Tdjsagdjhgasjd_123123"
    }
    res = post(headers, login_url, json.dumps(data))
    token = res.get("access")
    # user detail flow
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    user_detail_url = URL + "/users/auth/user/"
    data = {}
    get(headers, user_detail_url, json.dumps(data))
    
    # logout flow
    logout_url = URL + "/users/auth/logout/"
    data = {}
    post(headers, logout_url, json.dumps(data))

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    user_detail_url = URL + "/users/auth/user/"
    data = {}
    get(headers, user_detail_url, json.dumps(data))