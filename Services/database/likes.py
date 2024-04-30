from sqlalchemy.orm import Session
from Models.story_likes import Like
from Models.user import User
from Schemas.likes import LikeCreateSchema


def create_like(session: Session, like: LikeCreateSchema, token: str):
    current_user = User.get_current_user_by_token(token)
    owner_id = current_user['id']
    db_like = Like(**like.dict(), owner_id=owner_id)
    session.add(db_like)
    session.commit()
    session.refresh(db_like)
    return db_like

