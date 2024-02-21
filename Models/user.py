import jwt
from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    UniqueConstraint,
    PrimaryKeyConstraint
)

import settings
from database_initializer import Base

import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    first_name = Column(String(255), index=True, nullable=False)
    second_name = Column(String(255), index=True, nullable=False)
    patronymic = Column(String(255), index=True)
    hashed_password = Column(LargeBinary, nullable=False)

    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {full_name!r}>".format(full_name=self.first_name)

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
                {"first_name": self.first_name, "second_name": self.second_name, "patronymic": self.patronymic,
                 "email": self.email},
                settings.SECRET_KEY
            )
        }

    def generate_token(self) -> dict:
        """Сгенерируйте токен доступа для пользователя"""
        return {
            "access_token": jwt.encode(
                {"first_name": self.first_name, "second_name": self.second_name, "patronymic": self.patronymic,
                 "email": self.email},
                settings.SECRET_KEY
            )
        }
