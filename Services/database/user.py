from sqlalchemy.orm import Session

from Models.user import User
from Schemas.user import UserCreateSchema, UserBaseSchema, UserChangeSchema


def create_user(session: Session, user: UserCreateSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, user_name: str):
    return session.query(User).filter(User.user_name == user_name).one()


def change_user(session: Session, username:  str, user: UserChangeSchema):
    db_user = session.query(User).filter(User.user_name == username).one()
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    session.commit()
    session.refresh(db_user)
    return db_user

# def change_user(session: Session, user: UserBaseSchema):
#     user = session.query(User).filter(User.id == user.id).first()
#     user.user_name = user.user_name
#     user.first_name = user.first_name
#     user.second_name = user.second_name
#     user.patronymic = user.patronymic
#     session.commit()
#     return user
# def get_user_by_id(session: Session, user_id: int):
#     return session.query(User).filter(User.id == user_id).one()

