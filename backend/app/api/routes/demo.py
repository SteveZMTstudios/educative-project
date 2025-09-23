from fastapi import APIRouter

router = APIRouter(prefix="/demo", tags=["demo"])

fake_items = [
    {"id": 1, "title": "Shell 基础练习", "difficulty": "easy"},
    {"id": 2, "title": "用户匹配示例", "difficulty": "medium"},
]

@router.get("/items")
async def list_items():
    return fake_items

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return next((i for i in fake_items if i["id"] == item_id), None)
