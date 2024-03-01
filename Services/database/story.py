from sqlalchemy.orm import Session  # Импортируем класс Session для работы с сессиями SQLAlchemy
from Models.story import Story  # Импортируем модель Story
from Schemas.story import StoryCreateSchema  # Импортируем схему StoryCreateSchema для валидации данных


def create_story(session: Session, story: StoryCreateSchema):  # Функция для создания истории
    db_story = Story(**story.dict())  # Создаем новую историю из данных, полученных от пользователя
    session.add(db_story)  # Добавляем новую историю в сессию
    session.commit()  # Сохраняем изменения в базе данных
    session.refresh(db_story)  # Обновляем данные истории из базы данных
    return db_story  # Возвращаем созданную историю


def get_story_by_id(session: Session, story_id: int):  # Функция для получения истории по id
    return session.query(Story).filter(Story.id == story_id).one()  # Возвращаем историю с заданным id
