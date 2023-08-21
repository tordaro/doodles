import requests
from getpass import getpass

url = "https://api.zaptec.com/oauth/token"

username = input("Username: ")
password = getpass()

data = {"grant_type": "password", "username": username, "password": password}

response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, verify=False)

if response.status_code == 200:
    response_data = response.json()
    access_token = response_data.get("access_token")
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to obtain token. Status code: {response.status_code}, Error: {response.text}")
