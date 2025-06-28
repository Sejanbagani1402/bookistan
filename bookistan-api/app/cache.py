import redis
import json
import os

import redis.exceptions

REDIS_HOST = os.getenv("REDIS_HOST", "172.29.175.231")

REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(REDIS_HOST, REDIS_PORT, decode_responses=True)


def get_book_cache():
    try:
        cached = r.get("books")
        if cached:
            return json.loads(cached)
    except redis.exceptions.RedisError as re:
        print("The Redis is having error: ", re)
        return None


def set_book_cache(data):
    try:
        r.set("books", json.dumps(data))
    except redis.exceptions.RedisError as re:
        print("The Redis is having error: ", re)
        pass
