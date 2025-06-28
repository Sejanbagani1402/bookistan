from fastapi import HTTPException, Depends, APIRouter, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.cache import get_book_cache, set_book_cache

router = APIRouter(prefix="/books", tags=["books"])


# # GET /books (list all books) Status Code: 201
@router.get("/", status_code=status.HTTP_201_CREATED)
def show_books(db: Session = Depends(get_db)):
    cached_books = get_book_cache()
    if cached_books:
        return cached_books
    books = db.query(models.Book).all()
    result = [schemas.BookShow.model_validate(book) for book in books]
    set_book_cache([book.model_dump() for book in result])
    return result


# # POST /books (add a new book) Status Code: 201
@router.post("/", response_model=schemas.BookShow, status_code=status.HTTP_201_CREATED)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# # GET /books/{id}/reviews Status Code: 201
@router.get(
    "/{book_id}/reviews",
    response_model=list[schemas.ReviewShow],
    status_code=status.HTTP_201_CREATED,
)
def show_book_review(book_id: int, db: Session = Depends(get_db)):
    reviews = db.query(models.Reviews).filter(models.Reviews.book_id == book_id).all()
    return reviews


# # POST /books/{id}/reviews Status Code: 201
@router.post(
    "/{book_id}/reviews",
    response_model=schemas.ReviewShow,
    status_code=status.HTTP_201_CREATED,
)
def add_book_review(
    book_id: int, review: schemas.ReviewShow, db: Session = Depends(get_db)
):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_review = models.Reviews(content=review.content, book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
