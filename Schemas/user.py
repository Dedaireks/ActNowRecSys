from typing import List

from pydantic import BaseModel, EmailStr, Field  # Импортируем необходимые классы из библиотеки pydantic

from Schemas.post import PostBase
from Schemas.story import StoryCreateSchema


class UserBaseSchema(BaseModel):
    email: EmailStr
    user_name: str
    first_name: str
    second_name: str
    patronymic: str


class UserCreateSchema(UserBaseSchema):
    hashed_password: str = Field(alias="password")


class UserSchema(UserBaseSchema):
    id: int
    posts: List[PostBase] = []
    stories: List[StoryCreateSchema] = []

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(alias="Email")
    password: str


class UserChangeSchema(BaseModel):
    user_name: str
    first_name: str
    second_name: str
    patronymic: str
