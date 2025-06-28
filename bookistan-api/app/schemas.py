from pydantic import BaseModel
from typing import List


class ReviewCreate(BaseModel):
    content: str


class ReviewShow(BaseModel):
    id: int
    content: str

    class Config:
        from_attributes = True


class BookCreate(BaseModel):
    title: str
    author: str
    price: float | None
    description: str | None
    rating: str | None


class BookShow(BaseModel):
    id: int
    title: str
    author: str
    price: float | None
    description: str | None
    rating: float | None
    review: List[ReviewShow] = []

    class Config:
        from_attributes = True
