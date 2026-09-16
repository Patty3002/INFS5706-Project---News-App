# Personalised News Newsletter Agent — Project Skeleton

This is a setup-only skeleton for a school project. It contains no application functionality yet.

## Recommended stack

- Backend: Python + FastAPI
- Frontend: React + Vite
- Future database: SQLite for local development, or PostgreSQL/Supabase if deployed
- Future integrations: a news API, an AI API, an email service, and a scheduler

Python/FastAPI is recommended because the project will involve AI prompts, text processing, validation, and scheduled background work. React/Vite is a lightweight frontend that communicates with the backend through HTTP API endpoints.

## Project layout

```text
newsletter-agent-skeleton/
├── README.md
├── .gitignore
├── .env.example
├── backend/
│   ├── README.md
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       │   └── __init__.py
│       ├── core/
│       │   └── __init__.py
│       ├── models/
│       │   └── __init__.py
│       ├── services/
│       │   └── __init__.py
│       └── jobs/
│           └── __init__.py
├── frontend/
│   ├── README.md
│   ├── package.json
│   ├── index.html
│   ├── public/
│   │   └── .gitkeep
│   └── src/
│       ├── main.jsx
│       ├── api/
│       │   └── .gitkeep
│       ├── components/
│       │   └── .gitkeep
│       ├── pages/
│       │   └── .gitkeep
│       └── styles/
│           └── .gitkeep
└── docs/
    ├── architecture.md
    └── future-work.md
```

## Setup intention

The backend currently only creates a FastAPI application object. The frontend currently only mounts a static placeholder. Add functionality incrementally after confirming that both projects start successfully.

## Suggested next implementation order

1. Define preference data structures.
2. Add a preference API.
3. Add news-provider integration.
4. Add summary-generation service.
5. Add newsletter rendering.
6. Add email delivery.
7. Add scheduling and persistence.

Do not commit real API keys. Copy `.env.example` to `.env` locally when integrations are added.
