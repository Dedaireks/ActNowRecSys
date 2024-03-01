from typing import List

from pydantic import BaseModel, EmailStr, Field  # Импортируем необходимые классы из библиотеки pydantic

from Schemas.story import StoryCreateSchema


class UserBaseSchema(BaseModel):  # Базовая схема пользователя
    email: EmailStr  # Электронная почта пользователя
    user_name: str  # Имя пользователя
    first_name: str  # Имя пользователя
    second_name: str  # Фамилия пользователя
    patronymic: str  # Отчество пользователя


class UserCreateSchema(UserBaseSchema):  # Схема для создания пользователя
    hashed_password: str = Field(alias="password")  # Хешированный пароль пользователя


class UserSchema(UserBaseSchema):  # Схема пользователя для возврата данных пользователю из API (ответа)
    # и для валидации данных пользователя (запроса) в API
    id: int  # Уникальный идентификатор пользователя
    children: List[StoryCreateSchema] = []

    class Config:  # Класс для конфигурации схемы она нужна для того чтобы схема могла работать с атрибутами
        from_attributes = True  # Включаем режим from_attributes для совместимости с SQLAlchemy


class UserLoginSchema(BaseModel):  # Схема для входа пользователя
    email: EmailStr = Field(alias="Email")  # Электронная почта пользователя, используемая как имя пользователя
    password: str  # Пароль пользователя
