"""Backend application entry point.

This file intentionally contains setup only. Application routes and services
will be added in later project stages.
"""

from fastapi import FastAPI
from app.api import health


app = FastAPI(
    title="Personalised News Newsletter Agent",
    version="0.1.0",
)

app.include_router(health.router)
