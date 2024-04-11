from typing import Dict

import jwt
from fastapi import HTTPException, Depends
from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    UniqueConstraint,
    PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship
from starlette import status

import settings
from Routers.auth import oauth2_scheme
from database_initializer import Base

import bcrypt


#   from redis_initializer import redis


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    user_name = Column(String(255), index=True, unique=True)
    first_name = Column(String(255), index=True, nullable=False)
    second_name = Column(String(255), index=True, nullable=False)
    patronymic = Column(String(255), index=True)
    hashed_password = Column(LargeBinary, nullable=False)

    stories = relationship("Story", back_populates="owner")
    posts = relationship("Post", back_populates="owner")

    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")

    def __repr__(self):
        return "<User {user_name!r}>".format(user_name=self.user_name)

    @staticmethod
    def hash_password(password) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password) -> bool:
        return {
            "access_token": jwt.encode(
                {"user_name": self.user_name, "id": self.id},
                "ApplicationSecretKey"
            )
        }

    def generate_token(self) -> dict:
        return {
            "access_token": jwt.encode(
                {"user_name": self.user_name, "id": self.id},
                settings.SECRET_KEY
            )
        }

    def get_current_user_by_token(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )


# import uuid
# import redis
# from sqlalchemy import (
#         LargeBinary,
#         Column,
#         String,
#         Integer,
#         UniqueConstraint,
#         PrimaryKeyConstraint    )
#
# from database_initializer import Base
# import bcrypt
#
# # Создайте подключение к серверу Redis
# r = redis.Redis(host='actnow_redis_test2', port=6379, db=0)
#
# class User(Base):
#         __tablename__ = "users"
#
#         id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#         email = Column(String(255), unique=True, index=True)
#         first_name = Column(String(255), index=True, nullable=False)
#         second_name = Column(String(255), index=True, nullable=False)
#         patronymic = Column(String(255), index=True)
#         hashed_password = Column(LargeBinary, nullable=False)
#
#         UniqueConstraint("email", name="uq_user_email")
#         PrimaryKeyConstraint("id", name="pk_user_id")
#
#         def __repr__(self):
#             """Returns string representation of model instance"""
#             return "<User {full_name!r}>".format(full_name=self.first_name)
#
#         @staticmethod
#         def hash_password(password) -> str:
#             """Преобразование пароля из текстовой формы в
#             криптографические хэши
#             """
#             return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
#
#         def validate_password(self, password) -> bool:
#             """Подтверждает валидность пароля"""
#             return bcrypt.checkpw(password.encode(), self.hashed_password)
#
#         def generate_token(self) -> dict:
#             """Сгенерируйте уникальный идентификатор сессии и сохраните данные пользователя в Redis"""
#             token = str(uuid.uuid4())
#             user_data = {"first_name": self.first_name, "second_name": self.second_name, "patronymic": self.patronymic,
#                          "email": self.email}
#             redis.hmset(token, user_data)  # сохранить данные пользователя в Redis
#             return {"access_token": token}
