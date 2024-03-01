from pydantic import BaseModel, HttpUrl  # Импортируем классы BaseModel и HttpUrl из библиотеки pydantic
from typing import Optional  # Импортируем необходимые типы из модуля typing


# class StoryBaseSchema(BaseModel):  # Определяем схему для создания истории
#     id: int  # Уникальный идентификатор истории, необязательный параметр
#     user_id: int  # Уникальный идентификатор пользователя, создавшего историю
#     story_likes: int  # Количество лайков, полученных историей
#     story_descriptions: Optional[str]  # Краткое описание истории, необязательный параметр
#     link_to_goals: HttpUrl  # Ссылка на цели истории
#     content: HttpUrl  # Медиа-контент истории



class StoryCreateSchema(BaseModel):  # Определяем схему для создания истории
    owner_id: int  # Уникальный идентификатор пользователя, создавшего историю
    story_descriptions: Optional[str]  # Краткое описание истории, необязательный параметр
    link_to_goals: str  # Ссылка на цели истории
    content: str  # Медиа-контент истории
    class Config:  # Класс для конфигурации схемы
        from_attributes = True  # Включаем режим from_attributes для совместимости с SQLAlchemy
