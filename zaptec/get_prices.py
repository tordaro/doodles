import requests
from datetime import datetime


def get_daily_price(year: int, month: int, day, price_area: int) -> requests.Response:
    url = f"https://www.hvakosterstrommen.no/api/v1/prices/{year}/{month:0>2}-{day:0>2}_NO{price_area}.json"
    response = requests.get(url, verify=False)
    return response


def main():
    now = datetime.now()
    price_area = 4

    response = get_daily_price(now.year, now.month, now.day, price_area)

    if response.status_code == 200:
        print(f"Prices for {now.date()}: ")
        for hour in response.json():
            print(hour)
    else:
        print(f"Request failed with status code: {response.status_code}. Error: {response.text}")


if __name__ == "__main__":
    main()
