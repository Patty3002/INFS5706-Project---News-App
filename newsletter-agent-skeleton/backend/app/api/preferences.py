from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/preferences",
    tags=["preferences"],
)

class User(BaseModel):
    email: str
    categories: list[str]
    articles_per_category: int
    summary_detail: str
    frequency: str

@router.get("/preferences")
def get_preferences():
    user1 = User(email="hello@gmail.com", categories=["technology", "business"], articles_per_category=1, summary_detail="detailed", frequency="manual")
    return {
        "user": user1
    }
