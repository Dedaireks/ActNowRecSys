from sqlalchemy.orm import Session

from Models.user import User
from Schemas.user import UserCreateSchema


def create_user(session: Session, user: UserCreateSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, email: str):
    return session.query(User).filter(User.email == email).one()


def get_user_by_id(session: Session, id: int):
    return session.query(User).filter(User.id == id).one()
