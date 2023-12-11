import requests
from getpass import getpass


def request_token(username: str, password: str) -> requests.Response:
    url = "https://api.zaptec.com/oauth/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "password", "username": username, "password": password}

    response = requests.post(url, data=data, headers=headers, verify=False)
    return response


def main():
    username = input("Username: ")
    password = getpass()
    response = request_token(username, password)

    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data.get("access_token")
        print(f"Access Token: {access_token}")
    else:
        print(f"Failed to obtain token. Status code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    main()