import os
import requests
from dotenv import load_dotenv


def request_token(username: str, password: str) -> requests.Response:
    url = "https://api.zaptec.com/oauth/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "password", "username": username, "password": password}

    response = requests.post(url, data=data, headers=headers)
    return response


def main():
    load_dotenv()
    username = os.getenv("ZAPTEC_USERNAME")
    password = os.getenv("ZAPTEC_PASSWORD")
    response = request_token(username, password)

    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
    else:
        print(f"Failed to obtain token. Status code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    main()