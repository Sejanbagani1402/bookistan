
#  Bookistan API

A FastAPI-powered Book Review service with PostgreSQL, Redis caching, SQLAlchemy ORM, and Alembic for migrations.

---

##  Tasks Given

This project was built to fulfill the following technical assessment tasks:

1. **Develop a Book Review Service API** with the following RESTful endpoints:
   - `GET /books` – List all books
   - `POST /books` – Add a new book
   - `GET /books/{id}/reviews` – Retrieve reviews for a specific book
   - `POST /books/{id}/reviews` – Add a review to a specific book

2. **Document the API** using auto-generated OpenAPI/Swagger documentation.

3. **Design and implement database migrations** using Alembic.

4. **Optimize review retrieval performance** by adding an index on the `book_id` column in the `reviews` table.

5. **Integrate Redis caching** for the book list endpoint.

6. **Implement cache-first logic**:
   - First attempt to read from Redis
   - On cache miss, fetch from database and populate Redis
   - If Redis is down, fallback gracefully to the database

7. **Add robust error handling** for caching and database failures.

8. **Write automated tests**:
   - ✅ Unit tests for key endpoints
   - ✅ Integration test covering cache-miss behavior

---

##  Features

-  Add and fetch books with ratings, prices, and descriptions
-  Add and fetch reviews for books
-  PostgreSQL database with SQLAlchemy ORM
-  Redis caching for fast retrieval of book data
-  Alembic for database migrations
-  Unit and integration tests with `pytest`
-  OpenAPI docs at `/docs`

---

## 🛠 Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- Alembic
- Pytest

---

##  Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/bookistan-api.git
cd bookistan-api
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env` file

Create a `.env` file in the root directory and copy:

```env
DATABASE_URL=postgresql://postgres:post@localhost:5432/book_review_db
REDIS_URL=redis://172.29.175.231:6379
REDIS_HOST=172.29.175.231
REDIS_PORT=6379
```

---

##  Database Migrations (Alembic)

### Generate migration script:

```bash
alembic revision --autogenerate -m "Initial migration"
```

### Apply migrations:

```bash
alembic upgrade head
```

---

##  Running Tests

```bash
# Set PYTHONPATH to root of project
set PYTHONPATH=.

# Run tests
pytest tests/
```

---

##  Run the App

```bash
uvicorn app.main:app --reload
```

Then go to: [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  API Endpoints

### Books

- `GET /books` — List all books (cached)
- `POST /books` — Add a new book

### Reviews

- `GET /books/{id}/reviews` — Get reviews for a book
- `POST /books/{id}/reviews` — Add a review to a book

---

##  Redis Health Check

```bash
GET /ping-redis
```

---

##  Project Structure

```
bookistan-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── cache.py
│   └── routers/
│       └── book.py
│
├── alembic/
│   ├── env.py
│   └── versions/
│
├── tests/
│   ├── test_books.py
│   └── test_cache.py
│
├── alembic.ini
├── .env
├── requirements.txt
└── README.md
```

---

##  Author

**Sejan Bagani** — [GitHub](https://github.com/sejanbagani1402)

---

##  License

This project is for demonstration purposes only.
