from pydantic import BaseModel, EmailStr, Field


class AdminrBaseSchema(BaseModel):
    email: EmailStr


class AdminCreateSchema(AdminrBaseSchema):
    hashed_password: str = Field(alias="password")
