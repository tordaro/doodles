import os
import requests

endpoint_url = "https://api.zaptec.com/api/chargehistory"

access_token = os.getenv("ZAPTEC_TOKEN")

headers = {"Authorization": f"Bearer {access_token}"}

params = {"UserId": ""}

response = requests.get(endpoint_url, headers=headers, verify=False, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}. Error: {response.text}")
