from sqlalchemy.orm import Session
from Models.complaints_user import Complaint_user
from Models.complaint_post import Complaint_post
from Models.complaint_story import Complaint_story
from Schemas.complaints import ComplaintsPostSchema, ComplaintsUserSchema, ComplaintsStorySchema


def create_post_complaint(session: Session, complaint: ComplaintsPostSchema, post_id: int):
    db_complaint = Complaint_post(**complaint.dict(), post_id=post_id)
    session.add(db_complaint)
    session.commit()
    session.refresh(db_complaint)
    return db_complaint


def create_story_complaint(session: Session, complaint: ComplaintsStorySchema, story_id: int):
    db_complaint = Complaint_story(**complaint.dict(), story_id=story_id)
    session.add(db_complaint)
    session.commit()
    session.refresh(db_complaint)
    return db_complaint


def create_user_complaint(session: Session, complaint: ComplaintsUserSchema, user_id: int):
    db_complaint = Complaint_user(**complaint.dict(), user_id=user_id)
    session.add(db_complaint)
    session.commit()
    session.refresh(db_complaint)
    return db_complaint

