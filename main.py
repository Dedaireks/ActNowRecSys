import fastapi
from Routers.router import router


#   from redis_initializer import redis

app = fastapi.FastAPI()

app.include_router(router)
