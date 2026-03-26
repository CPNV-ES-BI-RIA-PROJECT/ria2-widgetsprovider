# RIA2 Widgets Provider

FastAPI service that exposes a simple, unified API to list widgets and retrieve a public widget link.

The provider implementation is selected at runtime through environment variables:

- `bucket`: fetches widget files from Bucket Service
- `metabase`: fetches cards and public links from Metabase

## Features

- Single API contract for multiple widget backends
- Runtime provider selection with `WIDGET_PROVIDER`
- Dependency injection via `dependency-injector`
- Focused provider unit tests with `pytest`

## API

Base URL (local default): `http://localhost:8000`

### List widgets

- Method: `GET`
- Path: `/widgets`
- Response: object mapping `widget_id -> widget_name`

Example response:

```json
{
	"first-widget.html": "First Widget",
	"second-widget.html": "Second Widget"
}
```

### Get widget public link

- Method: `GET`
- Path: `/widgets/{widget_id}`
- Response: public URL as a string
- Error: `404` when the widget does not exist

Example:

```bash
curl http://localhost:8000/widgets/first-widget.html
```

## Project Structure

```text
app/
	main.py                            # FastAPI app entrypoint
	controllers/widgets_controller.py  # HTTP routes
	config/container.py                # Dependency injection container
	services/widget_service/
		widget_service.py                # Service facade
		widget_provider_factory.py       # Provider selection
		models/
			bucket_widget_provider.py      # Bucket implementation
			metabase_widget_provider.py    # Metabase implementation
tests/
	widget_service/                    # Provider unit tests
examples/
	provider-bucket/docker-compose.yaml
	provider-metabase/docker-compose.yaml
```

## Requirements

- Python 3.14+ (recommended to match Docker image)
- pip
- Optional: Docker + Docker Compose

## Environment Configuration

1. Copy `.env.example` to `.env`.
2. Set common variables.
3. Uncomment and set only the variables needed for your selected provider.

### Common variables

| Variable | Required | Description |
| --- | --- | --- |
| `PORT` | No | API port (defaults to `8000`) |
| `WIDGET_PROVIDER` | Yes | `bucket` or `metabase` |

### Bucket provider variables

| Variable | Required when `WIDGET_PROVIDER=bucket` | Description |
| --- | --- | --- |
| `PROVIDER_BUCKET_NAME` | Yes | Bucket path/prefix used by Bucket Service |
| `PROVIDER_BUCKET_SERVICE_URL` | Yes | Bucket Service base URL (example: `http://bucket-service:8080`) |

### Metabase provider variables

| Variable | Required when `WIDGET_PROVIDER=metabase` | Description |
| --- | --- | --- |
| `PROVIDER_METABASE_SERVICE_URL` | Yes | Metabase base URL (example: `http://localhost:3000`) |
| `PROVIDER_METABASE_API_KEY` | Yes | Metabase API key used in `X-API-Key` header |

## Local Development Setup

### Install (development dependencies)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/dev.txt
```

### Run in development mode

```bash
python -m fastapi dev app/main.py
```

The service will start on `http://localhost:8000` by default.

## Run with Docker

### Option 1: Use published image with example compose files (Don't forget to fill the environment values)

Bucket provider stack:

```bash
docker compose -f examples/provider-bucket/docker-compose.yaml up -d
```

Metabase provider stack:

```bash
docker compose -f examples/provider-metabase/docker-compose.yaml up -d
```

### Option 2: Build and run locally

```bash
docker build -t ria2-widgetsprovider .
docker run --rm -p 8000:8000 --env-file .env ria2-widgetsprovider
```

## Testing

Run all tests:

```bash
python -m pytest
```

Run with coverage:

```bash
python -m pytest --cov
```

## Collaboration

Contributions are welcome.

1. Create a feature branch from your main integration branch.
2. Keep changes focused and include tests when behavior changes.
3. Run the test suite locally before opening a pull request.
4. Open a pull request with a clear description of the problem and solution.

Recommended local validation:

```bash
python -m pytest
```