# Python Expense Tracker (Django)

A clean, production‑ready Django application to track **inflows** (income) and **outflows** (expenses), visualize spending with **weekly / monthly / yearly** charts, and enforce savings goals. Built with a modular `src/` layout, pytest, and CI.

## Features
- User auth (signup/login/logout) with extended **UserProfile** (income, savings goal, income frequency)
- Create / edit / delete **Expense** records (category, amount, date, inflow/outflow, notes)
- **Dashboard** with Chart.js pie charts for **weekly / monthly / yearly** breakdowns
- Filter by date range; CSV export
- Environment‑based settings via `django-environ`
- `src/` layout, type hints, Ruff + Black linting, pytest tests, GitHub Actions CI

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.sample .env  # edit SECRET_KEY etc.
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and sign up.

## Project Structure
```
python-expense-tracker/
├─ src/
│  ├─ expense_tracker/            # Django project settings/urls
│  └─ apps/
│     ├─ accounts/                # signup, profile
│     ├─ expenses/                # CRUD for expenses
│     └─ dashboard/               # charts & summaries
├─ templates/                     # global templates
├─ static/                        # global static (css/js)
├─ tests/                         # pytest tests
├─ manage.py
├─ pyproject.toml                 # tooling + packaging
├─ requirements.txt
├─ .env.sample
├─ LICENSE
├─ README.md
└─ .github/workflows/ci.yml
```

## Environment
Create `.env` from sample:
```
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost
TIME_ZONE=Europe/Rome
```

## Test & Lint
```bash
pytest -q
ruff check .
ruff format .
```

## Charts
The dashboard uses **Chart.js** via CDN. Endpoints return JSON; the page renders interactive pie charts for weekly/monthly/yearly.

## License
MIT — see LICENSE.