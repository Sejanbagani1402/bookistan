from pydantic import BaseModel, ConfigDict
from typing import List


class ReviewCreate(BaseModel):
    content: str


class ReviewShow(BaseModel):
    id: int
    content: str

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BaseModel):
    title: str
    author: str
    price: float | None
    description: str | None
    rating: float | None


class BookShow(BaseModel):
    id: int
    title: str
    author: str
    price: float | None
    description: str | None
    rating: float | None
    review: List[ReviewShow] = []

    model_config = ConfigDict(from_attributes=True)
