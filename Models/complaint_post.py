from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, String
from sqlalchemy.orm import relationship

from database_initializer import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(String, index=True, nullable=False)

    post_id = Column(Integer, ForeignKey("post.id"), nullable=True)
    post = relationship("Post", back_populates="complaints")

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    owner = relationship("User", back_populates="complaints")

    story_id = Column(Integer, ForeignKey("stories.id"), nullable=True)
    story = relationship("Story", back_populates="complaints")
