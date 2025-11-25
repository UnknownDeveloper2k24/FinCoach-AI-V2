from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GoalCreate(BaseModel):
    name: str
    target_amount: float
    deadline: datetime
    monthly_savings_needed: Optional[float] = None

class GoalResponse(BaseModel):
    id: int
    user_id: int
    name: str
    target_amount: float
    current_amount: float
    deadline: datetime
    monthly_savings_needed: float
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class GoalUpdate(BaseModel):
    name: Optional[str] = None
    target_amount: Optional[float] = None
    deadline: Optional[datetime] = None
    status: Optional[str] = None
