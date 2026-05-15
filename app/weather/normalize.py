def normalize_ipma(data):

    today = data["data"][0]

    normalized = {
        "source": "ipma",
        "forecast_date": today["forecastDate"],
        "temp_min": float(today["tMin"]),
        "temp_max": float(today["tMax"]),
        "rain_probability": float(today["precipitaProb"]),
        "wind_direction": today["predWindDir"],
        "wind_class": int(today["classWindSpeed"]),
        "weather_type": int(today["idWeatherType"])
    }

    return normalized