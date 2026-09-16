from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/categories",
    tags=["categories"],
)

CATEGORY_LIST = [
    "world",
    "business",
    "technology",
    "science",
    "health",
    "sports",
    "entertainment",
    "Australia"
]

@router.get("/categories")
def get_categories():
    return {
        "categories": f"{CATEGORY_LIST}",
    }