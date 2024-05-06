import jwt
from settings import SECRET_KEY, TOKEN_EXPIRE_TIME, REDIS_LOGOUT_VALUE
import redis_initializer


def logout_user(token):
    # Сохраняем токен в Redis при выходе пользователя
    redis_initializer.r.setex(name=token, time=TOKEN_EXPIRE_TIME, value=REDIS_LOGOUT_VALUE)


def verify_token_in_redis(token):
    token_status = redis_initializer.r.get(token)
    if token_status is None:
        return True
    if token_status.decode('utf-8') == REDIS_LOGOUT_VALUE:
        return False
    try:
        jwt.decode(token, SECRET_KEY)
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    return True