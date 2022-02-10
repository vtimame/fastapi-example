from fastapi import APIRouter

router = APIRouter(prefix="/cats")


@router.get("/")
async def find_all_cats():
    return {"message": "Find all cats"}


@router.get("/{cat_id}")
async def find_all_cats(cat_id: str):
    return {"message": f"Find cat {cat_id}"}
