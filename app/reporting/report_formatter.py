def format_section(title, section):

    lines = []

    lines.append(title)

    for item in section["top"]:
        lines.append(f"• {item}")

    if section["outer"]:
        lines.append(f"• {section['outer']}")

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
    # Header
    #

    lines.append(
        f"Relatório roupa criança — {weather['forecast_date']}"
    )

    lines.append("")

    #
    # Weather summary
    #

    lines.append(
        f"🌡 {weather['temp_min']}°C → {weather['temp_max']}°C"
    )

    lines.append(
        f"🌧 Chuva: {weather['rain_probability']}%"
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

    return "\n".join(lines)