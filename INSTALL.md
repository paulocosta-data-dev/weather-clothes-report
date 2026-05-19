# Meteo — Installation Guide

This guide is intentionally beginner-friendly.

You do NOT need:
- programming experience,
- Docker experience,
- Linux knowledge.

---

# Step 1 — Install Docker Desktop

Download:

https://www.docker.com/products/docker-desktop/

Install Docker Desktop.

After installation:

- open Docker Desktop,
- wait until Docker is running.

---

# Step 2 — Create a GitHub account

Create a free account:

https://github.com/

---

# Step 3 — Download the project

On GitHub:

1. Click the green "Code" button.
2. Click "Download ZIP".
3. Extract the ZIP file.

---

# Step 4 — Create email configuration

Inside the project folder create:

```text
.env
```

Add:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_FROM=your_email@gmail.com
EMAIL_TO=destination_email@gmail.com
EMAIL_TO_2=optional_second_email@gmail.com
```

---

# Gmail users

Google blocks standard passwords.

You must create a Gmail App Password:

https://support.google.com/accounts/answer/185833

---

# Step 5 — Build the container

Open terminal inside the project folder.

Run:

```bash
docker build -t weather-report .
```

---

# Step 6 — Run the project locally

Run:

```bash
docker run --rm --env-file .env weather-report
```

You should receive an email.

---

# Step 7 — Create a GitHub token

Go to:

```text
GitHub → Settings → Developer settings → Personal access tokens
```

Required permissions:

- Actions → Read and write
- Workflows → Read and write
- Metadata → Read-only

---

# Step 8 — Create a cron-job.org account

https://cron-job.org

---

# Step 9 — Configure automation

## URL

```text
https://api.github.com/repos/YOUR_USER/weather-clothes-report/actions/workflows/weather-report.yml/dispatches
```

## Method

```text
POST
```

## Request body

```json
{
  "ref": "main"
}
```

## Headers

```text
Accept: application/vnd.github+json
Authorization: Bearer YOUR_GITHUB_TOKEN
X-GitHub-Api-Version: 2022-11-28
Content-Type: application/json
```

---

# Result

The project will:

- run automatically every day,
- fetch weather data,
- generate recommendations,
- send the email report.

Your PC does not need to stay on.