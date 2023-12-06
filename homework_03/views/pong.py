from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter(prefix="/ping", tags=["Ping"])
@router.get("/")
def pong():
    return {"message": "pong"}