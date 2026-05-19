# Meteo

Automated weather and clothing recommendation system focused on child thermal comfort, practical clothing guidance and fully automated daily delivery.

The project combines:

- weather APIs,
- rule-based reasoning,
- cloud scheduling,
- Docker execution,
- automated email delivery.

Instead of showing only weather forecasts, the system translates weather conditions into real-world recommendations:

- removable layers,
- thermal comfort,
- school-ready clothing,
- footwear,
- socks,
- night comfort,
- humidity discomfort,
- overnight thermal drops,
- rain windows during the day.

---

# Example output

```text
🌡 12°C → 20°C
🌧 Chuva: 0%

☀️

👕
• T-shirt
• Sweat manga comprida leve
• Corta vento leve removível

🩳
• Leggings ou calças leves

👟
• Ténis meia estação

🧦
• Meias leves

  - Saída de casa fresca
  - Tirar o corta vento na escola
  - Se aquecer durante a tarde pode ficar apenas com a sweat

🌙

🛌
• Pijama manga comprida leve

🧦
• Meias muito leves

  - Temperatura confortável ao adormecer
  - Descida térmica prevista de 6°C
  - Meias leves podem ajudar a manter conforto térmico
```

---

# Main features

## Hour-by-hour thermal analysis
The system analyses hourly weather evolution instead of relying only on daily averages.

## Rule-based recommendation engine
The recommendation system evaluates:

- temperature,
- apparent temperature,
- humidity,
- thermal drops,
- rain probability,
- time of day,
- removable layers,
- sleep comfort.

## Automated cloud execution
The pipeline runs automatically every day without requiring a local machine.

## Fully containerised
The project runs inside Docker for portability and reproducibility.

---

# Technologies

- Python
- Docker
- GitHub Actions
- cron-job.org
- SMTP
- Open-Meteo API
- IPMA API

---

# Architecture overview

```text
cron-job.org
    ↓
GitHub Actions
    ↓
Docker container
    ↓
Weather APIs
    ↓
Rule engine
    ↓
Formatted email report
```

---

# Why this project matters

This project demonstrates:

- real-world automation,
- API integration,
- operational thinking,
- cloud scheduling,
- rule-engine design,
- Dockerisation,
- practical product thinking,
- structured pipeline design.

It follows a clear data pipeline approach:

```text
Ingestion
→ Normalisation
→ Decision engine
→ Formatting
→ Delivery
```

---

# Repository structure

```text
weather-clothes-report/
│
├── .github/workflows/
│   └── weather-report.yml
│
├── app/
│   ├── main.py
│   │
│   ├── weather/
│   │   ├── ipma.py
│   │   ├── normalize.py
│   │   └── open_meteo.py
│   │
│   ├── rules/
│   │   └── clothing_rules.py
│   │
│   └── reporting/
│       ├── report_formatter.py
│       └── sender.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Additional documentation

- INSTALL.md
- ARCHITECTURE.md
- TRADEOFFS.md