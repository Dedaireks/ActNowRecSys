from pydantic import BaseModel


class StoryCreateSchema(BaseModel):
    descriptions: str
    content: str
    post_id: int


class Story(StoryCreateSchema):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class StoryChangeSchema(BaseModel):
    descriptions: str
    content: str

    class Config:
        from_atributes = True
