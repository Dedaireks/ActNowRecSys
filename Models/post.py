from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

from database_initializer import Base


class Goals(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    stories_count_by_goal = Column(Integer, index=True)
    goal_favorites_count = Column(Integer, index=True)
    goal_cost = Column(Integer, index=True)
    goal_event_date = Column(Date, index=True)
    goal_event_time = Column(Time, index=True)
    goal_location = Column(String, index=True)
    goal_description = Column(String, index=True)
    goal_title = Column(String, index=True)
    goal_owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    stories = relationship("Story", back_populates="posts")
    owner = relationship("User", back_populates="posts")
