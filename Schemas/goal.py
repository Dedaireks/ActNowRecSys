from pydantic import BaseModel
from  datetime import date, time


class GoalBase(BaseModel):
    stories_count_by_goal: int
    goal_favorites_count: int
    goal_cost: int
    goal_event_date: date
    goal_event_time: time
    goal_location: str
    goal_description: str
    goal_title: str
    goal_owner_id: int

    class Config:
        from_attributes = True
