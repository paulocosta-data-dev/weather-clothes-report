import requests
from weather.http_client import fetch_json


URL = (
    "https://api.ipma.pt/open-data/"
    "forecast/meteorology/cities/daily/1110600.json"
)


def fetch_weather():
    return fetch_json(URL)