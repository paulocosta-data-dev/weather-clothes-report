def build_period_recommendation(top, outer=None, notes=None):

    return {
        "top": top,
        "outer": outer,
        "notes": notes or []
    }


WIND_CLASS_DESCRIPTION = {
    1: "fraco",
    2: "moderado",
    3: "forte"
}


def needs_rain_jacket(weather):

    return weather["rain_probability"] >= 30


def needs_light_jacket(weather):

    return (
        weather["wind_class"] >= 3
        and weather["temp_min"] <= 12
    )


def get_temperature_profile(weather):

    temp_min = weather["temp_min"]
    temp_max = weather["temp_max"]

    #
    # Cold
    #

    if temp_min <= 10:
        return "cold"

    #
    # Mild
    #

    if temp_min <= 16:
        return "mild"

    #
    # Hot
    #

    if temp_max >= 30:
        return "hot"

    #
    # Warm
    #

    return "warm"


def generate_clothing_recommendation(weather):

    recommendation = {}

    profile = get_temperature_profile(weather)

    #
    # Morning
    #

    morning_notes = []

    outer = None

    if needs_rain_jacket(weather):

        outer = "impermeável leve"

        morning_notes.append(
            "levar proteção para chuva"
        )

    elif needs_light_jacket(weather):

        outer = "casaco corta-vento leve"

        morning_notes.append(
            "vento mais forte durante a manhã"
        )

    #
    # Cold morning
    #

    if profile == "cold":

        recommendation["morning"] = build_period_recommendation(
            top=[
                "t-shirt manga comprida",
                "hoodie leve"
            ],
            outer=outer,
            notes=[
                "criança ativa, usar camadas removíveis",
                *morning_notes
            ]
        )

    #
    # Mild morning
    #

    elif profile == "mild":

        recommendation["morning"] = build_period_recommendation(
            top=[
                "t-shirt manga comprida leve",
                "hoodie leve"
            ],
            outer=outer,
            notes=[
                "remover hoodie se aquecer durante o dia",
                *morning_notes
            ]
        )

    #
    # Hot morning
    #

    elif profile == "hot":

        recommendation["morning"] = build_period_recommendation(
            top=[
                "t-shirt manga curta"
            ],
            notes=[
                "evitar excesso de roupa logo pela manhã"
            ]
        )

    #
    # Warm morning
    #

    else:

        recommendation["morning"] = build_period_recommendation(
            top=[
                "t-shirt leve"
            ],
            outer=outer,
            notes=morning_notes
        )

    #
    # Afternoon
    #

    afternoon_notes = []

    outer = None

    if needs_rain_jacket(weather):

        outer = "impermeável leve"

        afternoon_notes.append(
            "possibilidade de chuva durante a tarde"
        )

    #
    # Cold afternoon
    #

    if profile == "cold":

        recommendation["afternoon"] = build_period_recommendation(
            top=[
                "t-shirt manga comprida leve",
                "hoodie leve"
            ],
            outer=outer,
            notes=[
                "temperatura fresca durante o dia",
                *afternoon_notes
            ]
        )

    #
    # Mild afternoon
    #

    elif profile == "mild":

        recommendation["afternoon"] = build_period_recommendation(
            top=[
                "t-shirt manga comprida leve"
            ],
            outer=outer,
            notes=[
                "temperatura amena durante a tarde",
                *afternoon_notes
            ]
        )

    #
    # Hot afternoon
    #

    elif profile == "hot":

        recommendation["afternoon"] = build_period_recommendation(
            top=[
                "t-shirt manga curta"
            ],
            notes=[
                "evitar excesso de roupa devido à atividade física"
            ]
        )

    #
    # Warm afternoon
    #

    else:

        recommendation["afternoon"] = build_period_recommendation(
            top=[
                "t-shirt leve"
            ],
            outer=outer,
            notes=afternoon_notes
        )

    #
    # Evening
    #

    evening_notes = []

    outer = None

    if needs_light_jacket(weather):

        outer = "casaco leve"

        evening_notes.append(
            "vento mais fresco ao final do dia"
        )

    #
    # Cold evening
    #

    if profile == "cold":

        recommendation["evening"] = build_period_recommendation(
            top=[
                "hoodie leve"
            ],
            outer=outer,
            notes=evening_notes
        )

    #
    # Mild evening
    #

    elif profile == "mild":

        recommendation["evening"] = build_period_recommendation(
            top=[
                "t-shirt manga comprida leve"
            ],
            outer=outer,
            notes=evening_notes
        )

    #
    # Hot evening
    #

    elif profile == "hot":

        recommendation["evening"] = build_period_recommendation(
            top=[
                "t-shirt leve"
            ],
            notes=[
                "temperatura ainda elevada ao final do dia"
            ]
        )

    #
    # Warm evening
    #

    else:

        recommendation["evening"] = build_period_recommendation(
            top=[
                "t-shirt leve"
            ],
            outer=outer,
            notes=evening_notes
        )

    return recommendation