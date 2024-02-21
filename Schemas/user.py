from pydantic import BaseModel, EmailStr, Field


class UserBaseSchema(BaseModel):
    email: EmailStr
    first_name: str
    second_name: str
    patronymic: str


class UserCreateSchema(UserBaseSchema):
    hashed_password: str = Field(alias="password")


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(alias="username")
    password: str
