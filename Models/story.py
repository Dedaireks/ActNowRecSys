from sqlalchemy import (
    Column,  # Модуль для создания столбцов в таблице
    String,  # Модуль для работы со строковыми данными
    Integer,  # Модуль для работы с целочисленными данными
    PrimaryKeyConstraint, ForeignKey  # Модуль для создания первичных ключей
)
from sqlalchemy.orm import relationship

from database_initializer import Base  # Импортируем базовый класс для моделей


class Story(Base):  # Класс Story наследуется от базового класса моделей
    __tablename__ = "storys"  # Указываем имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Создаем столбец 'id',
    # который является первичным ключом и автоинкрементируется
    story_owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)  # Создаем столбец 'owner_id',
    # который содержит id пользователя, который опубликовал историю

    story_likes = Column(Integer, unique=False, index=True)  # Создаем столбец 'story_likes',
    # который содержит количество лайков истории
    story_descriptions = Column(String(2550), index=True, nullable=True)  # Создаем столбец 'story_descriptions',
    # который содержит описание истории
    story_content = Column(String(2550), nullable=False)
    # Создаем столбец 'content', который содержит контент истории
    PrimaryKeyConstraint("id", name="pk_story_id")  # Устанавливаем ограничение
    # первичного ключа на столбец 'id'

    owner = relationship("User", back_populates="storys")
    # Создаем связь между таблицами 'storys' и 'users', чтобы получить информацию о владельце истории
    # через атрибут 'storys' у объекта 'User'. Связь один-ко-многим, где
    # один пользователь может иметь много историй
    goal = relationship("Goals", back_populates="storys")
    # Создаем связь между таблицами 'storys' и 'goals',
    # чтобы получить информацию о целях истории, через атрибут 'storys' у объекта 'Goals'.
    # Связь один-ко-многим, где одна цель может иметь много историй
