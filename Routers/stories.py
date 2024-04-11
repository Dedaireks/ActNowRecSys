from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from Models.story import Story
from Models.user import User
from Schemas.story import StoryCreateSchema, StoryChangeSchema
from Services.database.story import get_story_by_id, create_story, get_all_user_stories, change_story
from Services.database.user import get_user
from database_initializer import get_db
from typing import List

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/stories", response_model=StoryCreateSchema)
def create_story_endpoint(story: StoryCreateSchema,
                          token: str = Depends(oauth2_scheme),
                          db: Session = Depends(get_db)):
    return create_story(session=db, story=story, token=token)


@router.get("/get_stories", response_model=List[StoryCreateSchema])
def get_all_stories(db: Session = Depends(get_db)):
    return db.query(Story).all()


@router.get("/stories/{story_id}", response_model=StoryCreateSchema)
def read_story(story_id: int, db: Session = Depends(get_db)):
    story = get_story_by_id(db, story_id=story_id)

    if story is None:
        raise HTTPException(status_code=404, detail="История не найдена")

    return story


@router.get("/users/{username}/stories_by_username", response_model=List[StoryCreateSchema])
def read_user_stories(username: str, db: Session = Depends(get_db)):
    user = get_user(db, user_name=username)

    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    stories = get_all_user_stories(db, owner_id=user.id)
    return stories


@router.delete("/stories/{story_id}")
def delete_story(story_id: int,
                 db: Session = Depends(get_db),
                 token: str = Depends(oauth2_scheme)):

    story = get_story_by_id(db, story_id=story_id)
    user = User.get_current_user_by_token(token)
    user_id = user['id']

    if story.owner_id != user_id:
        raise HTTPException(status_code=403, detail="У вас нет прав на удаление этого поста")

    if story is None:
        raise HTTPException(status_code=404, detail="История не найдена")

    db.delete(story)
    db.commit()
    return {"message": "История успешно удалена"}


@router.patch("/stories_change/{story_id}")
def update_story(
        story_id: int,
        storyscheme: StoryChangeSchema,
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)):
    story = get_story_by_id(db, story_id=story_id)
    user = User.get_current_user_by_token(token)
    user_id = user["id"]
    if story.owner_id != user_id:
        raise HTTPException(status_code=403, detail="У вас нет прав на изменение этой истории")
    if story is None:
        raise HTTPException(status_code=404, detail="История не найдена")
    change_story(story_id=story_id, session=db, story=storyscheme)
    return {"message": "История изменена"}