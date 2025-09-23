# CMLRE Marine Data Platform (Backend)

## Quick Start

1. Create `.env` from example and set secrets.
2. Build and run services:

```bash
docker compose up -d --build
```

API will be at `http://localhost:8000`, docs at `/docs` and `/redoc`.

## Development

- Python 3.12+
- Install with Poetry:

```bash
pip install poetry
poetry install
uvicorn app.main:app --reload
```

## Documentation

- [Developer Guide](DEVELOPER_GUIDE.md) - Comprehensive guide for new developers
- API Documentation: Available at `/docs` (Swagger) and `/redoc` (ReDoc) when running

## Environment

See `.env.example` for keys like `DATABASE_URL`, `GEMINI_API_KEY`, and MinIO settings.
