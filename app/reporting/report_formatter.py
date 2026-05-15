def format_section(title, section):

    lines = []

    lines.append(title)

    for item in section["top"]:
        lines.append(f"• {item}")

    if section["outer"]:
        lines.append(f"• {section['outer']}")

    for item in section["sleep_layers"]:
        lines.append(f"• {item}")

    if section["notes"]:

        for note in section["notes"]:
            lines.append(f"  - {note}")

    lines.append("")

    return lines


def format_report_email(report):

    weather = report["weather"]
    recommendation = report["recommendation"]

    lines = []

    #
    # Weather summary
    #

    lines.append(
        f"🌡 {round(weather['temp_min'])}°C → {round(weather['temp_max'])}°C"
    )

    lines.append(
        f"🌧 Chuva: {round(weather['rain_probability'])}%"
    )

    lines.append("")

    #
    # Morning
    #

    lines.extend(
        format_section(
            "☀️ Manhã",
            recommendation["morning"]
        )
    )

    #
    # Afternoon
    #

    lines.extend(
        format_section(
            "🌤 Tarde",
            recommendation["afternoon"]
        )
    )

    #
    # Evening
    #

    lines.extend(
        format_section(
            "🌙 Final do dia",
            recommendation["evening"]
        )
    )

    #
    # Night
    #

    lines.extend(
        format_section(
            "😴 Dormir",
            recommendation["night"]
        )
    )

    return "\n".join(lines)