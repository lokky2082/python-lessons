from fastapi import FastAPI, Query
from typing import Annotated
from views import pong

app = FastAPI()
app.include_router(pong)
@app.get("/")
def hello():
    return {"message": "Hello World"}
