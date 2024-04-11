from sqlalchemy import (
    Column,
    String,
    Integer,
    PrimaryKeyConstraint, ForeignKey
)
from sqlalchemy.orm import relationship

from database_initializer import Base


class Story(Base):  #
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    #story_likes = Column(Integer, unique=False, index=True)
    descriptions = Column(String(2550), index=True, nullable=True)
    content = Column(String(2550), nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="stories")

    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    posts = relationship("Post", back_populates="stories")

    PrimaryKeyConstraint("id", name="pk_story_id")
