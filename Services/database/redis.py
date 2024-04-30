# import jwt
# import redis
# from fastapi import HTTPException
#
# from settings import SECRET_KEY, TOKEN_EXPIRE_TIME
#
# try:
#     r = redis.Redis(host='redis', port=6379, password='redis')
# except redis.exceptions.ConnectionError as err:
#     raise HTTPException(status_code=500, detail=f"Не удалось подключиться к Redis: {err}")
#
#
# def logout_user(token):
#     # Сохраняем токен в Redis при выходе пользователя
#     r.setex(name=token, time=TOKEN_EXPIRE_TIME, value='logged_out')
#
#
# def verify_token_in_redis(token):
#     if r.get(token) is None:
#         return False
#     try:
#         jwt.decode(token, SECRET_KEY)
#     except jwt.ExpiredSignatureError:
#         return False
#     except jwt.InvalidTokenError:
#         return False
#     return True
