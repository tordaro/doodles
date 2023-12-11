import os
import requests
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def request_charge_history(
    access_token: str, installation_id: str, from_date: datetime, to_date: datetime
) -> requests.Response:
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    endpoint_url = "https://api.zaptec.com/api/chargehistory"
    params = {
        "InstallationId": installation_id,
        "GroupBy": "2",
        "DetailLevel": "1",
        "From": from_date.strftime(datetime_format),
        "To": to_date.strftime(datetime_format),
    }
    headers = {"accept": "application/json", "Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(endpoint_url, headers=headers, params=params)
        print(response.headers)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    return response


def main():
    access_token = os.getenv("ZAPTEC_TOKEN")
    installation_id = os.getenv("INSTALLATION_ID")
    from_date = datetime(year=2023, month=9, day=1)
    to_date = datetime(year=2023, month=9, day=5)
    response = request_charge_history(access_token, installation_id, from_date, to_date)

    if response.status_code == 200:
        data = response.json()["Data"]
        for session in data:
            pprint(session["EnergyDetails"])
            pprint(session["Energy"])
            pprint(session["UserFullName"])
            pprint(session["StartDateTime"])
            pprint(session["EndDateTime"])
            pprint(session["DeviceName"])
            print()
    else:
        print(f"Request failed with status code: {response.status_code}. Error: {response.text}")


if __name__ == "__main__":
    main()
