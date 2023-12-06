from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter(prefix="/items", tags=["Items"])

class CreateItemScheme(BaseModel):
    name: str

@router.get("/")
def items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "foobar"
            },
            {
                "id": 1,
                "name": "fizzbuzz"
            }
        ]
    }
@router.get("{item_id}/")
def get_item(item_id: int):
    return {
       "data": {
           "id": item_id,
           "name": f"foobar{item_id}"
       } 
    }
@router.post("/")
def create_item(item: CreateItemScheme):
    return {
        "data": {
            "id": 10,
            **item.model_dump()
        }
    }