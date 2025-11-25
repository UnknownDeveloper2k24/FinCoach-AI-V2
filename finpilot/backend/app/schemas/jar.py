from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JarCreate(BaseModel):
    name: str
    target_amount: float
    priority: int = 1
    deadline: Optional[datetime] = None
    color: str = "bg-blue-500"

class JarResponse(BaseModel):
    id: int
    user_id: int
    name: str
    target_amount: float
    current_amount: float
    priority: int
    deadline: Optional[datetime]
    color: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class JarUpdate(BaseModel):
    target_amount: Optional[float] = None
    current_amount: Optional[float] = None
    priority: Optional[int] = None
    deadline: Optional[datetime] = None
