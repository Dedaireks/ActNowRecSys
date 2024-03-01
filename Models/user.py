import jwt
from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    UniqueConstraint,
    PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship

import settings
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
    storys = relationship("Story", back_populates="owner")

    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")


    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {user_name!r}>".format(user_name=self.user_name)

    @staticmethod
    def hash_password(password) -> str:
        """Преобразование пароля из текстовой формы в
        криптографические хэши
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password) -> bool:
        """Подтверждает валидность пароля"""
        return {
            "access_token": jwt.encode(
                {"user_name": self.user_name, "email": self.email},
                "ApplicationSecretKey"
            )
        }

    def generate_token(self) -> dict:
        """Generate access token for user"""
        return {
            "access_token": jwt.encode(
                {"user_name": self.user_name, "email": self.email},
                settings.SECRET_KEY
            )
        }

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
