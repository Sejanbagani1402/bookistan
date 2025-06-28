import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from sqlalchemy.orm import Session
from app.database import SessionLocal

db: Session = SessionLocal()
from sqlalchemy import text

# print(db.execute(text("SELECT * FROM books")).fetchall())

db.execute(text("INSERT INTO books (title, author) VALUES ('1984', 'George Orwell')"))
db.commit()
print(db.execute(text("SELECT * FROM books")).fetchall())
