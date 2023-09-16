import os
from typing import Iterable
import requests
from datetime import datetime, timedelta
from pprint import pprint


def request_daily_price(date: datetime, price_area: int, cert_path: str = "") -> requests.Response:
    url = (
        "https://www.hvakosterstrommen.no/api/v1/prices/"
        + f"{date.year}/{date.month:0>2}-{date.day:0>2}_NO{price_area}.json"
    )

    if cert_path:
        response = requests.get(url, verify=cert_path)
    else:
        response = requests.get(url, verify=False)

    return response


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
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(endpoint_url, headers=headers, verify=False, params=params)
    return response


def calculate_price(data: list[dict], prices: dict[str, list]) -> dict[str, dict]:
    datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    user_totals: dict[str, dict] = {}

    for session in data:
        user = session.setdefault("UserFullName", "Unknown")
        device = session["DeviceName"]
        total_session_energy = session["Energy"]
        energy_details = session["EnergyDetails"]

        total_cost = 0
        energy_pr_period = []
        price_pr_period = []
        for energy_entry in energy_details:
            timestamp = datetime.strptime(energy_entry["Timestamp"], datetime_format)
            timestamp += timedelta(hours=2)  # Shift to UTC+2
            energy = energy_entry["Energy"]
            energy_pr_period.append(energy)

            price = prices[str(timestamp.date())][timestamp.hour]["NOK_per_kWh"]
            total_cost += price * energy
            price_pr_period.append(price)

        if user in user_totals:
            user_totals[user]["total_cost"] += total_cost
            user_totals[user]["devices"].add(device)
            user_totals[user]["energy_pr_period"].extend(energy_pr_period)
            user_totals[user]["price_pr_period"].extend(price_pr_period)
            user_totals[user]["energy_pr_session"].append(total_session_energy)
        else:
            user_totals[user] = {}
            user_totals[user]["energy_pr_period"] = energy_pr_period
            user_totals[user]["energy_pr_session"] = [total_session_energy]
            user_totals[user]["price_pr_period"] = price_pr_period
            user_totals[user]["total_cost"] = total_cost
            user_totals[user]["devices"] = set(device)

    for user in user_totals:
        user_totals[user]["avg_price"] = sum(user_totals[user]["price_pr_period"]) / len(
            user_totals[user]["price_pr_period"]
        )
        user_totals[user]["total_energy"] = sum(user_totals[user]["energy_pr_period"])
    return user_totals


def main():
    access_token = os.getenv("ZAPTEC_TOKEN")
    installation_id = "5fdd61e6-989b-4d2e-ab75-68e1ee9141cf"
    from_date = datetime(year=2023, month=8, day=5)
    to_date = datetime(year=2023, month=9, day=14)
    charge_history = request_charge_history(access_token, installation_id, from_date, to_date)
    if charge_history.status_code == 200:
        session_data = charge_history.json()["Data"]
    else:
        print(f"Request failed with status code: {charge_history.status_code}. Error: {charge_history.text}")

    price_area = 4
    cert_path = "hvakosterstrommen-no-chain.pem"
    prices = {}
    days = (to_date - from_date).days
    date = from_date.date()
    for day in range(-2, days + 1):
        lookup_date = date + timedelta(days=day)
        daily_price = request_daily_price(date=lookup_date, price_area=price_area, cert_path=cert_path)
        if daily_price.status_code == 200:
            prices[str(lookup_date)] = daily_price.json()
        else:
            print(f"Request failed with status code: {daily_price.status_code}. Error: {daily_price.text}")

    pprint(calculate_price(session_data, prices))


if __name__ == "__main__":
    main()
