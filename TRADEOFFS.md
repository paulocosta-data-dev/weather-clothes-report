# Engineering trade-offs

This project intentionally prioritised:

- simplicity,
- explainability,
- reliability,
- operational ease.

The following trade-offs were consciously made.

---

# Rule engine vs Machine Learning

## Chosen

Rule-based system.

## Rejected

Machine learning recommendation engine.

## Why

The project needs:

- explainable decisions,
- deterministic outputs,
- fast iteration,
- predictable behaviour.

For parenting decisions, transparent reasoning is more valuable than probabilistic prediction.

---

# Dual weather APIs

## Chosen

IPMA + Open-Meteo.

## Rejected

Single weather provider.

## Why

IPMA provides good regional Portuguese forecasts but limited hourly detail.

Open-Meteo provides stronger hourly granularity.

Combining both improved:

- hourly modelling,
- night comfort analysis,
- rain timing,
- thermal transitions.

Trade-off:

- higher integration complexity,
- multiple schemas,
- more normalisation logic.

---

# Docker vs Local execution

## Chosen

Docker containers.

## Rejected

Native local execution.

## Why

Docker guarantees:

- reproducibility,
- portability,
- isolated dependencies,
- easier cloud execution.

Trade-off:

- additional setup complexity for beginners.

---

# cron-job.org vs GitHub scheduler

## Chosen

External scheduling through cron-job.org.

## Rejected

Native GitHub Actions cron scheduling.

## Why

GitHub scheduled workflows showed reliability issues on low-activity repositories.

cron-job.org proved significantly more stable.

Trade-off:

- one additional external dependency.

---

# SMTP vs notification platforms

## Chosen

SMTP email delivery.

## Rejected

Telegram, WhatsApp or mobile push notifications.

## Why

Email:

- is universal,
- requires no mobile app,
- works across devices,
- is easy to automate.

Trade-off:

- slower interaction model,
- less real-time UX.

---

# Cloud execution vs local scheduling

## Chosen

Cloud automation.

## Rejected

Local PC execution.

## Why

Cloud execution avoids:

- powered-on dependency,
- home network issues,
- local failures,
- energy waste.

Trade-off:

- dependency on third-party services.

---

# Structured formatting vs raw weather data

## Chosen

Human-oriented recommendations.

## Rejected

Generic weather summaries.

## Why

The objective is:

```text
decision support
```

not:

```text
weather display
```

Trade-off:

- more opinionated outputs,
- larger ruleset,
- subjective comfort modelling.

---

# Simplicity vs completeness

The project intentionally does NOT model:

- indoor temperature sensors,
- child metabolism,
- clothing materials,
- live body temperature,
- dynamic sleep tracking.

This keeps:

- maintenance low,
- behaviour predictable,
- deployment simple.

Trade-off:

- lower precision.

---

# Final engineering philosophy

The project prioritises:

```text
practical reliability over technical complexity
```

The goal was never to build the most advanced weather engine.

The goal was to build:

- a maintainable system,
- a realistic automation pipeline,
- useful recommendations,
- deterministic behaviour,
- operational simplicity.