from fastapi import FastAPI
from app.routers import book
import os


app = FastAPI(title="Book review service")
app.include_router(book.router)

import redis


@app.get("/")
def root():
    return {"message": "Book Review API is running!"}


@app.get("/ping-redis")
def ping_redis():
    try:
        REDIS_HOST = os.getenv("REDIS_HOST", "172.29.175.231")
        REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
        r = redis.Redis(REDIS_HOST, REDIS_PORT, decode_responses=True)
        pong = r.ping()
        return {"redis": "connected" if pong else "not connected"}
    except Exception as e:
        return {"error": str(e)}
