from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import Sessionlocal, engine, get_db

app = FastAPI()


# GET /books (list all books)
@app.get("/books")
async def ShowBooks():
    return None


# POST /books (add a new book)
@app.post("/books")
async def AddBook():
    return None


# GET /books/{id}/reviews
@app.get("/books/{id}/reviews")
async def AddReview():
    return None


# POST /books/{id}/reviews
@app.post("/books/{id}/reviews")
async def ShowReviews():
    return None
