from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Index, Float
from sqlalchemy.orm import Relationship
from app.database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float)
    description = Column(String)
    rating = Column(Float)
    review = Relationship("Reviews", back_populates="book")


class Reviews(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    content = Column(Text, nullable=False)
    book = Relationship("Book", back_populates="review")
    __table_args__ = (Index("ix_reviews_book_id", "book_id"),)
