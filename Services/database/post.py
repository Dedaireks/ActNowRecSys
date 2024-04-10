from sqlalchemy.orm import Session  # Импортируем класс Session для работы с сессиями SQLAlchemy
from Models.post import Goals # Импортируем модель Story
from Schemas.post import PostBase


def create_goal(session: Session, goal: PostBase):  # Функция для создания истории
    db_goal = Goals(**goal.dict())  # Создаем новую историю из данных, полученных от пользователя
    session.add(db_goal)  # Добавляем новую историю в сессию
    session.commit()  # Сохраняем изменения в базе данных
    session.refresh(db_goal)  # Обновляем данные истории из базы данных
    return db_goal  # Возвращаем созданную историю


def get_story_by_id(session: Session, goal_id: int):  # Функция для получения истории по id
    return session.query(Goals).filter(Goals.id == goal_id).one()  # Возвращаем историю с заданным id
