from pydantic import BaseModel


class TagsCreate(BaseModel):
    value: str
    owner_id: int
    post_id: int
    story_id: int


class Tags(TagsCreate):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True