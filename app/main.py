import json
import requests
from pathlib import Path

from weather.normalize import normalize_ipma
from rules.clothing_rules import generate_clothing_recommendation
from reporting.report_formatter import format_report_email
from reporting.sender import send_email

URL = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"

OUTPUT_DIR = Path("/app/output")
OUTPUT_FILE = OUTPUT_DIR / "report.json"


def fetch_weather():

    response = requests.get(URL, timeout=10)

    response.raise_for_status()

    return response.json()


def save_report(report):

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)


def main():

    raw_data = fetch_weather()

    weather = normalize_ipma(raw_data)
    
    ##weather = {
    ##"forecast_date": "2026-03-12",
    ##"temp_min": 15,
    ##"temp_max": 19,
    ##"rain_probability": 0,
    ##"wind_direction": "N",
    ##"wind_class": 3,
    ##"weather_type": 2
    ##}

    recommendation = generate_clothing_recommendation(weather)

    result = {
        "weather": weather,
        "recommendation": recommendation
    }

    save_report(result)

    formatted_email = format_report_email(result)

    print(formatted_email)
    
    send_email(
    subject="Relatório roupa criança",
    body=formatted_email
    )


if __name__ == "__main__":
    main()