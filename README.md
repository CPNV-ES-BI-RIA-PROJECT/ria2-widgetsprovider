# RIA2 - WidgetsProvider

## Before anything

Copy-paste the `.env.example` file to `.env` and fill the required information.

You need to run this service if you choose the `bucket` provider : [Bucket Service](https://github.com/diogof648-dev/bi-bucketservice/tree/develop) (Please refer to the project's README to run it)

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

### Coverage
```
python -m pytest --cov
```
You can visually see the coverage after typing the command using [this extension](https://marketplace.visualstudio.com/items?itemName=markis.code-coverage) on Visual Studio Code.


## Run

### Dev
```bash
python -m fastapi dev app/main.py
```

### Prod
```bash
docker compose up
```