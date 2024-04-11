from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

from Models.user import User
from database_initializer import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    favorites_count = Column(Integer, index=True, nullable=True)
    cost = Column(Integer, index=True, nullable=True)
    event_date = Column(Date, index=True)
    event_time = Column(Time, index=True)
    location = Column(String, index=True)
    description = Column(String, index=True)
    title = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    owner = relationship("User", back_populates="posts")

    stories = relationship("Story", back_populates="posts")



