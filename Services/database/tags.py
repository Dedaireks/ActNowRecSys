from fastapi import Depends
from sqlalchemy.orm import Session
from Models.tags import Tags
from Schemas.tags import TagBase
from database_initializer import get_db


def create_tag(tag: TagBase, session: Session = Depends(get_db)):
    db_tag = Tags(**tag.dict())
    session.add(db_tag)
    session.commit()
    session.refresh(db_tag)
    return db_tag

