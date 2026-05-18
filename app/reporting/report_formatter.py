def format_report_email(report):

    weather = report["weather"]

    rain_windows = (
        report["rain_windows"]
    )

    recommendation = (
        report["recommendation"]
    )

    lines = []

    #
    # Header
    #

    lines.append(
        (
            f"🌡 "
            f"{round(weather['temp_min'])}°C"
            f" → "
            f"{round(weather['temp_max'])}°C"
        )
    )

    lines.append(
        (
            f"🌧 Chuva: "
            f"{round(weather['rain_probability'])}%"
        )
    )

    #
    # Rain windows
    #

    if rain_windows:

        lines.append("")

        lines.append(
            "☔"
        )

        for rain in rain_windows:

            lines.append(
                (
                    f"• {rain['hour']} "
                    f"({rain['probability']}%)"
                )
            )

    lines.append("")

    #
    # Day
    #

    day = recommendation["day"]

    #
    # Torso
    #

    lines.append("☀️")

    lines.append("👕")

    for item in day["torso"]:

        lines.append(
            f"• {item}"
        )

    lines.append("")

    #
    # Legs
    #

    if day["legs"]:

        lines.append(
            "🩳"
        )

        lines.append(
            f"• {day['legs']}"
        )

        lines.append("")

    #
    # Footwear
    #

    if day["footwear"]:

        lines.append(
            "👟"
        )

        lines.append(
            f"• {day['footwear']}"
        )

        lines.append("")

    #
    # Socks
    #

    if day["socks"]:

        lines.append(
            "🧦"
        )

        lines.append(
            f"• {day['socks']}"
        )

    #
    # Notes
    #

    if day["notes"]:

        lines.append("")

        for note in day["notes"]:

            formatted_note = (
                note[0].upper()
                + note[1:]
            )

            lines.append(
                f"  - {formatted_note}"
            )

    lines.append("")

    #
    # Night
    #

    night = recommendation["night"]

    lines.append("🌙")

    #
    # Sleep layers
    #

    lines.append("🛌")

    for layer in (
        night["sleep_layers"]
    ):

        lines.append(
            f"• {layer}"
        )

    lines.append("")

    #
    # Sleep socks
    #

    if night["sleep_socks"]:

        lines.append(
            "🧦"
        )

        lines.append(
            (
                f"• "
                f"{night['sleep_socks']}"
            )
        )

    #
    # Night notes
    #

    if night["notes"]:

        lines.append("")

        for note in (
            night["notes"]
        ):

            formatted_note = (
                note[0].upper()
                + note[1:]
            )

            lines.append(
                f"  - {formatted_note}"
            )

    return "\n".join(lines)