from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.cache import get_book_cache, set_book_cache

router = APIRouter(prefix="/books", tags=["books"])


# # GET /books (list all books)
# @app.get("/books")
# async def ShowBooks():
#     return None
@router.get("/")
def show_books(db: Session = Depends(get_db)):
    cached_books = get_book_cache()
    if cached_books:
        return cached_books

    books = db.query(models.Book).all()

    ###Hey, This could be wrong. Maybe it needa a check...
    schemas.BookShow.model_config["from_attributes"] = True
    result = [schemas.BookShow.model_validate]
    set_book_cache([books.dict() for book in result])
    return result


# # POST /books (add a new book)
# @app.post("/books")
# async def AddBook():
#     return None
@router.post("/", response_model=schemas.BookShow)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.model_dump())  ###This could be wrong I dont knowww
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# # GET /books/{id}/reviews
# @app.get("/books/{id}/reviews")
# async def AddReview():
#     return None
@router.get("/{book_id}/reviews", response_model=list[schemas.ReviewShow])
def show_book_review(book_id: int, db: Session = Depends(get_db)):
    reviews = db.query(models.Reviews).filter(models.Reviews.book_id == book_id).all()
    return reviews


# # POST /books/{id}/reviews
# @app.post("/books/{id}/reviews")
# async def ShowReviews():
#     return None
@router.post("/{book_id}/reviews", response_model=schemas.ReviewShow)
def add_book_review(book_id: int, review: schemas, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_review = models.Reviews(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
