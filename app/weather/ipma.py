import requests


URL = (
    "https://api.ipma.pt/open-data/"
    "forecast/meteorology/cities/daily/1110600.json"
)


def fetch_weather():

    response = requests.get(
        URL,
        timeout=10
    )

    response.raise_for_status()

    return response.json()