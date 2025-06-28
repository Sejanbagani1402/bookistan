<div align = "center"> 
 <h1>Bookistan</h1>
 <h2> It is a assesment project given by Predusk Technology Pvt. Ltd. </h2>
 <h3> This project is made by Sejan Khan. </h3>
</div>

---


# Tasks Given: 

1. Build a Book Review Service API with the following RESTful endpoints:

 - `GET` `/books` – Retrieve a list of all books

 - `POST` `/books`– Add a new book

 - `GET` `/books/{id}/reviews` – Retrieve all reviews for a specific book

 - `POST` `/books/{id}/reviews` – Add a review to a specific book

2. Auto-generate API documentation using OpenAPI/Swagger (via FastAPI docs).

3. Implement database migrations using Alembic.

4. Optimize review queries by adding an index on the book_id column in the reviews table.

5. Integrate Redis for caching the book list.

6. Implement cache-first strategy: Attempt to fetch from Redis first; if cache miss, fallback to database and populate the cache.

7. Add robust error handling for Redis connection failures.

8. Write tests:

 - ✅ Unit tests for core endpoints

 - ✅ Integration test covering cache miss fallback

---



A simple Book Review REST API built with **FastAPI**, **PostgreSQL**, **Redis**, and **SQLAlchemy**.

This project is a technical assessment for a Backend Engineer role. It includes:
- Book & Review APIs
- Redis integration for caching
- PostgreSQL persistence with migrations
- Swagger documentation
- Unit & integration tests

---

##  Tech Stack

- **Backend Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Caching:** Redis
- **Migrations:** Alembic
- **Testing:** Pytest
- **Documentation:** Swagger UI (auto-generated)

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sejanbagani1402/bookistan
cd bookistan
```
### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv/bin/activate 

```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv/bin/activate 

```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables

```bash
DATABASE_URL=postgresql://username:password@localhost:5432/book_review_db
REDIS_URL=redis://localhost:6379/0
```
### 5. Run Database Migrations

```bash
alembic upgrade head
```
### 6. Start Redis and PostgreSQL

```bash
docker-compose up -d

```
### 7. Run the FastAPI Server
```bash
uvicorn app.main:app --reload
```

Visit Swagger UI: [Link]http://localhost:8000/docs



 ### API Endpoints
 Books
`GET` `/books` – List all books (cached with Redis)

`POST` `/books` – Add a new book

Reviews
`GET` `/books/{book_id}/reviews` – Get reviews for a book

`POST` `/books/{book_id}/reviews` – Add a review to a book

### Caching Logic
On calling GET /books:

Tries to fetch book list from Redis

If cache miss, fetches from database, stores in Redis

If Redis is down, the app logs the error and fallbacks to database.

### Author
Sejan Bagani
LinkedIn • GitHub

 Notes
No authentication is implemented (per assessment instructions)

Error handling added for DB and Redis failures

Redis TTL can be configured inside cache.py

### How to Extend
GraphQL Subscriptions:

Use WebSockets with Strawberry/FastAPI

Define subscription { reviewAdded(bookId: ID!) }

Use Redis pub/sub for real-time push

Add auth via JWT for real-time subscriptions





