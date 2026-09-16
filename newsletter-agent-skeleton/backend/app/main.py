"""Backend application entry point.

This file intentionally contains setup only. Application routes and services
will be added in later project stages.
"""

from fastapi import FastAPI


app = FastAPI(
    title="Personalised News Newsletter Agent",
    version="0.1.0",
)
