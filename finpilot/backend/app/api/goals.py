from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/api/goals", tags=["goals"])

class Goal(BaseModel):
    title: str
    target_amount: float

@router.get("/")
def get_goals(db: Session = Depends(get_db)):
    return {"goals": []}

@router.post("/")
def create_goal(goal: Goal, db: Session = Depends(get_db)):
    return {"message": "Goal created", "data": goal}
