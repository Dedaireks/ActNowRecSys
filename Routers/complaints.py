from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from Schemas.complaints import ComplaintsCreate, ComplaintsPostSchema, ComplaintsStorySchema, ComplaintsUserSchema
from database_initializer import get_db

from Services.database.complaint import create_post_complaint, create_user_complaint, create_story_complaint
from Models.post import Post
from Models.story import Story
from Models.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/complaint/post{id}", response_model=ComplaintsPostSchema)
def create_complaint_post(complaint: ComplaintsPostSchema,
                          post_id: int,
                          token: str = Depends(oauth2_scheme),
                          db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=403, detail="Пост не найден")
    else:
        return create_post_complaint(session=db, complaint=complaint, post_id=post_id), {"message": "Жалоба отправлена"}


@router.post("/complaint/story{id}", response_model=ComplaintsCreate)
def create_complaint_story(complaint: ComplaintsStorySchema,
                           story_id: int,
                           token: str = Depends(oauth2_scheme),
                           db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=403, detail="История не найдена")
    else:
        return create_story_complaint(complaint=complaint, story_id=story_id, session=db), {"message": "Жалоба "
                                                                                                       "отправлена"}


@router.post("/complaint/user{id}", response_model=ComplaintsUserSchema)
def create_complaint_user(complaint: ComplaintsUserSchema,
                          user_id: int,
                          token: str = Depends(oauth2_scheme),
                          db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=403, detail="Пользователь не найден")
    else:
        return create_user_complaint(session=db, complaint=complaint, user_id=user_id), {"message": "Жалоба "
                                                                                                    "отправлена"}
