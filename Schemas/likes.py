# from pydantic import BaseModel
#
#
# class LikeCreateSchema(BaseModel):
#     value: int
#
#
# class Like(LikeCreateSchema):
#     id: int
#
#     class Config:
#         orm_mode = True
#         from_attributes = True
#