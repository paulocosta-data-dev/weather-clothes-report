import json

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

from weather.ipma import fetch_weather

from weather.normalize import (
    normalize_ipma
)

from weather.open_meteo import (
    fetch_hourly_weather,
    normalize_hourly_weather,
    filter_relevant_hours,
    get_rain_windows
)

from rules.clothing_rules import (
    generate_clothing_recommendation
)

from reporting.report_formatter import (
    format_report_email
)

from reporting.sender import (
    send_email
)


OUTPUT_DIR = Path(
    "/app/output"
)

OUTPUT_FILE = (
    OUTPUT_DIR / "report.json"
)


def save_report(report):

    OUTPUT_DIR.mkdir(
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False,
            default=str
        )


def main():

    #
    # Daily weather
    #

    raw_weather = (
        fetch_weather()
    )

    weather = normalize_ipma(
        raw_weather
    )

    #
    # Hourly weather
    #

    raw_hourly_weather = (
        fetch_hourly_weather()
    )

    normalized_hourly_weather = (
        normalize_hourly_weather(
            raw_hourly_weather
        )
    )

    hourly_weather = (
        filter_relevant_hours(
            normalized_hourly_weather
        )
    )

    #
    # Rain windows
    #

    rain_windows = (
        get_rain_windows(
            hourly_weather
        )
    )

    #
    # Recommendation
    #

    recommendation = (
        generate_clothing_recommendation(
            weather,
            hourly_weather
        )
    )

    #
    # Final payload
    #

    result = {
        "weather": weather,
        "hourly_weather": (
            hourly_weather
        ),
        "rain_windows": (
            rain_windows
        ),
        "recommendation": (
            recommendation
        )
    }

    #
    # Save
    #

    save_report(result)

    #
    # Format email
    #

    formatted_email = (
        format_report_email(
            result
        )
    )

    print(
        formatted_email
    )

    #
    # Email subject
    #

    timestamp = datetime.now(
        ZoneInfo(
            "Europe/Lisbon"
        )
    ).strftime(
        "%Y-%m-%d %H:%M"
    )

    #
    # Send email
    #

    send_email(
        subject=(
            f"Meteo - {timestamp}"
        ),
        body=formatted_email
    )


if __name__ == "__main__":

    main()