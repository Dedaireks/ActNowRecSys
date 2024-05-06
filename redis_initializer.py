import redis
from fastapi import HTTPException
from settings import REDIS_PORT, REDIS_HOST

try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
except redis.exceptions.ConnectionError as err:
    raise HTTPException(status_code=500, detail=f"Не удалось подключиться к Redis: {err}")