# RIA2 - WidgetsProvider

## Before anything

Copy-paste the `.env.example` file to `.env` and fill the required information.

## Installation DEV
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/dev.txt
```

## Installation PROD
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/prod.txt
```

## Tests
```bash
python -m pytest
```

## Run

### Dev
```bash
python -m fastapi dev app/main.py
```

### Prod
```bash
docker compose up
```