import os
import json
import urllib3
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

http = urllib3.PoolManager()

def request_charge_history(
    access_token: str, installation_id: str, from_date: datetime, to_date: datetime
) -> urllib3.response.HTTPResponse:
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    endpoint_url = "https://api.zaptec.com/api/chargehistory"
    params = {
        "InstallationId": installation_id,
        "GroupBy": "2",
        "DetailLevel": "1",
        "From": from_date.strftime(datetime_format),
        "To": to_date.strftime(datetime_format),
    }
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json-patch+json"}

    response = http.request('GET', endpoint_url, headers=headers, fields=params)

    return response


def main():
    access_token = os.getenv("ZAPTEC_TOKEN")
    installation_id = os.getenv("INSTALLATION_ID")
    from_date = datetime(year=2023, month=9, day=1)
    to_date = datetime(year=2023, month=9, day=5)
    response = request_charge_history(access_token, installation_id, from_date, to_date)

    if response.status == 200:
        data = json.loads(response.data)["Data"]
        for session in data:
            pprint(session["EnergyDetails"])
            pprint(session["Energy"])
            pprint(session["UserFullName"])
            pprint(session["StartDateTime"])
            pprint(session["EndDateTime"])
            pprint(session["DeviceName"])
            print()
    else:
        print(f"Request failed with status code: {response.status}. Error: {response.data.decode('utf-8')}")


if __name__ == "__main__":
    main()
