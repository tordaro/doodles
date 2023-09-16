import requests
from datetime import datetime


def get_daily_price(date: datetime, price_area: int, cert_path: str = "") -> requests.Response:
    url = (
        "https://www.hvakosterstrommen.no/api/v1/prices/"
        + f"{date.year}/{date.month:0>2}-{date.day:0>2}_NO{price_area}.json"
    )
    response = requests.get(url, verify=cert_path)
    return response


def main():
    now = datetime.now()
    price_area = 4
    cert_path = "hvakosterstrommen-no-chain.pem"

    response = get_daily_price(now, price_area, cert_path=cert_path)

    if response.status_code == 200:
        print(f"Prices for {now.date()}: ")
        for hour in response.json():
            print(hour)
    else:
        print(f"Request failed with status code: {response.status_code}. Error: {response.text}")


if __name__ == "__main__":
    main()
