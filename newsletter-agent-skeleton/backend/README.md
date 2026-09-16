# Backend skeleton

## Local setup

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The backend intentionally has no routes or application logic yet.

## Planned areas

- `api/`: HTTP route modules
- `core/`: configuration and shared infrastructure
- `models/`: request, response, and persistence models
- `services/`: news, AI, newsletter, and email integrations
- `jobs/`: future scheduled newsletter jobs
