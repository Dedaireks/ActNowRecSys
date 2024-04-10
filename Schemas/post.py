from pydantic import BaseModel
from datetime import date, time


class GoalBase(BaseModel):
    goal_event_date: date
    goal_event_time: time
    goal_location: str
    goal_description: str
    goal_title: str

    class Config:
        from_attributes = True
