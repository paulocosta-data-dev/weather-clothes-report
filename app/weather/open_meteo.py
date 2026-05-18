import requests

from datetime import datetime
from zoneinfo import ZoneInfo


URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=38.83"
    "&longitude=-9.17"
    "&hourly="
    "temperature_2m,"
    "apparent_temperature,"
    "relative_humidity_2m,"
    "precipitation_probability,"
    "wind_speed_10m"
    "&timezone=Europe%2FLisbon"
)


def fetch_hourly_weather():

    response = requests.get(
        URL,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def normalize_hourly_weather(hourly_data):

    hourly = hourly_data["hourly"]

    times = hourly["time"]

    temperatures = hourly["temperature_2m"]

    apparent_temperatures = (
        hourly["apparent_temperature"]
    )

    humidity = (
        hourly["relative_humidity_2m"]
    )

    precipitation = (
        hourly["precipitation_probability"]
    )

    wind_speed = (
        hourly["wind_speed_10m"]
    )

    result = []

    for (
        time,
        temp,
        apparent,
        hum,
        rain,
        wind
    ) in zip(
        times,
        temperatures,
        apparent_temperatures,
        humidity,
        precipitation,
        wind_speed
    ):

        parsed_time = (
            datetime.fromisoformat(time)
        )

        result.append(
            {
                "time": parsed_time,
                "temperature": temp,
                "apparent_temperature": (
                    apparent
                ),
                "humidity": hum,
                "rain_probability": rain,
                "wind_speed": wind
            }
        )

    return result


def filter_relevant_hours(
    hourly_weather
):

    portugal_tz = ZoneInfo(
        "Europe/Lisbon"
    )

    now = datetime.now(
        portugal_tz
    )

    today = now.date()

    relevant = []

    for hour_data in hourly_weather:

        hour_time = (
            hour_data["time"]
        )

        if (
            hour_time.date() == today
            or (
                hour_time.date() > today
                and hour_time.hour <= 7
            )
        ):

            relevant.append(
                hour_data
            )

    return relevant


def get_hour_temperature(
    hourly_weather,
    target_hour
):

    for hour_data in hourly_weather:

        if (
            hour_data["time"].hour
            == target_hour
        ):

            return (
                hour_data["temperature"]
            )

    return None


def get_rain_windows(
    hourly_weather
):

    rain_windows = []

    for hour_data in hourly_weather:

        rain_probability = (
            hour_data[
                "rain_probability"
            ]
        )

        if rain_probability >= 40:

            hour = (
                hour_data["time"]
                .strftime("%H:%M")
            )

            rain_windows.append(
                {
                    "hour": hour,
                    "probability": (
                        round(
                            rain_probability
                        )
                    )
                }
            )

    return rain_windows