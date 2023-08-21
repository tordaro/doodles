import os
import json
import requests

endpoint_url = "https://api.zaptec.com/api/chargehistory/installationreport"

access_token = os.getenv("ZAPTEC_TOKEN")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json-patch+json",
}

data = {
    "fromDate": "2023-08-01T11:47:19.986Z",
    "endDate": "2023-08-21T11:47:19.986Z",
    "installationid": "",
    "userids": [""],
    "chargerids": [""],
    "groupby": 0,
}

response = requests.post(endpoint_url, headers=headers, data=json.dumps(data), verify=False)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}. Error: {response.text}")
