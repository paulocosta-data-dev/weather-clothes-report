from weather.open_meteo import (
    get_hour_temperature
)


def build_period_recommendation(
    torso=None,
    legs=None,
    footwear=None,
    socks=None,
    sleep_layers=None,
    sleep_socks=None,
    notes=None
):

    return {
        "torso": torso or [],
        "legs": legs,
        "footwear": footwear,
        "socks": socks,
        "sleep_layers": sleep_layers or [],
        "sleep_socks": sleep_socks,
        "notes": notes or []
    }


def get_hour_data(
    hourly_weather,
    target_hour
):

    for hour_data in hourly_weather:

        if hour_data["time"].hour == target_hour:

            return hour_data

    return None


def calculate_cold_score(
    temperature,
    humidity,
    apparent_temperature
):

    score = 0

    if temperature <= 9:
        score += 5

    elif temperature <= 11:
        score += 4

    elif temperature <= 13:
        score += 3

    elif temperature <= 16:
        score += 2

    elif temperature <= 19:
        score += 1

    if humidity >= 90:
        score += 3

    elif humidity >= 80:
        score += 2

    elif humidity >= 70:
        score += 1

    if apparent_temperature <= (
        temperature - 3
    ):

        score += 2

    elif apparent_temperature <= (
        temperature - 1
    ):

        score += 1

    return score


def get_day_strategy(hourly_weather):

    morning = get_hour_data(
        hourly_weather,
        7
    )

    if morning is None:

        return {
            "torso": [
                "T-shirt",
                "Sweat manga comprida leve"
            ],
            "legs": (
                "Calças leves"
            ),
            "footwear": (
                "Ténis meia estação"
            ),
            "socks": (
                "Meias leves"
            ),
            "notes": []
        }

    cold_score = calculate_cold_score(
        temperature=morning["temperature"],
        humidity=morning["humidity"],
        apparent_temperature=(
            morning["apparent_temperature"]
        )
    )

    if cold_score >= 7:

        return {
            "torso": [
                "T-shirt",
                "Sweat manga comprida",
                "Casaco corta vento"
            ],
            "legs": (
                "Collants e "
                "calças grossas"
            ),
            "footwear": (
                "Ténis meia estação"
            ),
            "socks": (
                "Meias médias"
            ),
            "notes": [
                (
                    "manhã fria "
                    "e húmida"
                ),
                (
                    "remover o casaco "
                    "quando aquecer"
                )
            ]
        }

    if cold_score >= 4:

        return {
            "torso": [
                "T-shirt",
                (
                    "Sweat manga "
                    "comprida leve"
                ),
                (
                    "Corta vento "
                    "leve removível"
                )
            ],
            "legs": (
                "Leggings ou "
                "calças leves"
            ),
            "footwear": (
                "Ténis meia estação"
            ),
            "socks": (
                "Meias leves"
            ),
            "notes": [
                (
                    "saída de casa "
                    "fresca"
                ),
                (
                    "tirar o corta vento "
                    "na escola"
                ),
                (
                    "se aquecer durante "
                    "a tarde pode ficar "
                    "apenas com a sweat"
                )
            ]
        }

    if cold_score >= 2:

        return {
            "torso": [
                (
                    "T-shirt manga "
                    "comprida leve"
                ),
                (
                    "Sweat leve "
                    "removível"
                )
            ],
            "legs": (
                "Calças leves"
            ),
            "footwear": (
                "Ténis leves"
            ),
            "socks": (
                "Meias leves"
            ),
            "notes": [
                (
                    "temperatura "
                    "amena"
                )
            ]
        }

    return {
        "torso": [
            "T-shirt manga curta"
        ],
        "legs": (
            "Calções ou vestido"
        ),
        "footwear": (
            "Ténis respiráveis"
        ),
        "socks": (
            "Meias finas"
        ),
        "notes": [
            (
                "evitar excesso "
                "de roupa"
            )
        ]
    }


def get_sleep_strategy(hourly_weather):

    evening = get_hour_data(
        hourly_weather,
        21
    )

    dawn = get_hour_data(
        hourly_weather,
        3
    )

    if (
        evening is None
        or dawn is None
    ):

        return {
            "layers": [
                "Pijama leve"
            ],
            "socks": None,
            "notes": []
        }

    evening_temp = evening["temperature"]

    dawn_temp = dawn["temperature"]

    dawn_humidity = dawn["humidity"]

    dawn_apparent = (
        dawn["apparent_temperature"]
    )

    thermal_drop = (
        evening_temp - dawn_temp
    )

    cold_score = calculate_cold_score(
        temperature=dawn_temp,
        humidity=dawn_humidity,
        apparent_temperature=dawn_apparent
    )

    notes = []

    if evening_temp >= 19:

        notes.append(
            (
                "temperatura confortável "
                "ao adormecer"
            )
        )

    elif evening_temp <= 14:

        notes.append(
            (
                "quarto fresco logo "
                "ao início da noite"
            )
        )

    if dawn_humidity >= 85:

        notes.append(
            (
                "humidade elevada "
                "durante a madrugada"
            )
        )

    elif dawn_humidity >= 70:

        notes.append(
            (
                "alguma humidade "
                "durante a madrugada"
            )
        )

    if thermal_drop >= 7:

        notes.append(
            (
                "descida térmica prevista "
                f"de {round(thermal_drop)}°C"
            )
        )

    if cold_score >= 7:

        return {
            "layers": [
                (
                    "Body interior leve"
                ),
                (
                    "Pijama manga "
                    "comprida quente"
                )
            ],
            "socks": (
                "Meias leves"
            ),
            "notes": notes + [
                (
                    "conservar calor "
                    "durante a madrugada"
                ),
                (
                    "pés podem arrefecer "
                    "durante a noite"
                )
            ]
        }

    if cold_score >= 5:

        return {
            "layers": [
                (
                    "Pijama manga "
                    "comprida leve"
                )
            ],
            "socks": (
                "Meias leves"
            ),
            "notes": notes + [
                (
                    "temperatura mais fresca "
                    "durante a madrugada"
                ),
                (
                    "pés podem perder calor "
                    "durante a noite"
                )
            ]
        }

    if (
        evening_temp >= 20
        and thermal_drop >= 6
    ):

        return {
            "layers": [
                (
                    "Pijama leve "
                    "respirável"
                )
            ],
            "socks": None,
            "notes": notes + [
                (
                    "evitar sobreaquecimento "
                    "ao adormecer"
                ),
                (
                    "o quarto poderá "
                    "arrefecer durante "
                    "a madrugada"
                )
            ]
        }

    if cold_score >= 3:

        return {
            "layers": [
                (
                    "Pijama manga "
                    "comprida leve"
                )
            ],
            "socks": (
                "Meias muito leves"
            ),
            "notes": notes + [
                (
                    "temperatura relativamente "
                    "estável durante a noite"
                ),
                (
                    "meias leves podem ajudar "
                    "a manter conforto térmico"
                )
            ]
        }

    return {
        "layers": [
            "Pijama leve"
        ],
        "socks": None,
        "notes": notes + [
            (
                "evitar excesso "
                "de calor"
            )
        ]
    }


def generate_clothing_recommendation(
    weather,
    hourly_weather
):

    day = get_day_strategy(
        hourly_weather
    )

    sleep = get_sleep_strategy(
        hourly_weather
    )

    recommendation = {}

    recommendation["day"] = (
        build_period_recommendation(
            torso=day["torso"],
            legs=day["legs"],
            footwear=day["footwear"],
            socks=day["socks"],
            notes=day["notes"]
        )
    )

    recommendation["night"] = (
        build_period_recommendation(
            sleep_layers=sleep["layers"],
            sleep_socks=sleep["socks"],
            notes=sleep["notes"]
        )
    )

    return recommendation