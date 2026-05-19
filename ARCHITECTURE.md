# Architecture

## Objective

Convert raw weather data into actionable clothing recommendations.

The system focuses on:

- child comfort,
- thermal regulation,
- removable layers,
- sleep comfort,
- practical decision-making.

---

# High-level flow

```text
cron-job.org
    ↓
GitHub Actions
    ↓
Docker execution
    ↓
Weather ingestion
    ↓
Normalisation
    ↓
Rule engine
    ↓
Formatted report
    ↓
SMTP delivery
```

---

# Weather ingestion

## IPMA

Used for:

- min/max temperature,
- daily forecast,
- rain probability,
- weather classification.

## Open-Meteo

Used for:

- hourly temperature,
- apparent temperature,
- humidity,
- wind,
- hourly rain probability.

---

# Why two APIs?

IPMA provides strong Portuguese regional forecasts but limited hourly modelling.

Open-Meteo provides detailed hourly data.

Combining both improves:

- granularity,
- thermal modelling,
- night analysis,
- rain timing.

---

# Normalisation layer

The project converts different API structures into a unified internal model.

This reduces coupling between:

- external APIs,
- business logic,
- reporting.

---

# Rule engine

The recommendation engine is entirely rule-based.

Inputs include:

- temperature,
- apparent temperature,
- humidity,
- thermal drops,
- wind,
- rain probability,
- time of day.

Outputs include:

- torso layers,
- footwear,
- socks,
- night clothing,
- thermal notes,
- rain warnings.

---

# Why rules instead of ML?

This system prioritises:

- explainability,
- deterministic behaviour,
- easy tuning,
- predictable outputs.

For parenting-related decisions, transparent reasoning is more valuable than opaque prediction.

---

# Reporting layer

The report formatter converts structured recommendations into human-readable email output.

Focus areas:

- readability,
- quick scanning,
- emoji grouping,
- contextual notes,
- practical language.

---

# Automation

## Scheduling

cron-job.org triggers GitHub Actions through the GitHub API.

## Execution

GitHub Actions:

- builds the Docker image,
- runs the container,
- sends the report.

---

# Security

Secrets are managed using:

- GitHub Secrets,
- environment variables,
- local `.env` files.

Sensitive credentials are excluded from Git.

---

# Operational concerns addressed

- scheduler reliability,
- cloud execution,
- reproducibility,
- secret management,
- portability,
- deterministic execution,
- dependency isolation.