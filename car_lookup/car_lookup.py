import os
import requests


def get_vehicle_data(api_key: str, license_plate: str) -> dict:
    url = "https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata"

    headers = {"SVV-Authorization": f"Apikey {api_key}"}
    params = {"kjennemerke": license_plate}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Request failed with status {response.status_code}: {response.text}")


if __name__ == "__main__":
    api_key = str(os.environ.get("VEGVESENET_API_KEY"))
    license_plate = input("Enter the license plate (e.g., EB11111): ")

    response = get_vehicle_data(api_key, license_plate)
    technical_data = response["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]
    brand = technical_data["generelt"]["merke"][0]["merke"]
    model = technical_data["generelt"]["handelsbetegnelse"][0]
    color = technical_data["karosseriOgLasteplan"]["rFarge"][0]["kodeNavn"]

    print(f"{color} {brand} {model}")
