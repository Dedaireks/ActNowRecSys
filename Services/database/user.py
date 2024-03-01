from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from Models.user import User
from Schemas.user import UserCreateSchema


def create_user(session: Session, user: UserCreateSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, user_name: str): # Функция для получения пользователя по имени
    return session.query(User).filter(User.user_name == user_name).one()


def get_user_by_id(session: Session, user_id: int): # Функция для получения пользователя по id
    return session.query(User).filter(User.id == user_id).one()

def get_all_user_stories(session: Session, user_id: int): # Функция для получения
    # всех историй пользователя по его id
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        storys_data = jsonable_encoder(user.storys)
        return storys_data   # Возвращаем все истории пользователя
    else:
        return None
