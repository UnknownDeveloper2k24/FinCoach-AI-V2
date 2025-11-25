from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlertCreate(BaseModel):
    type: str
    severity: str = "info"
    message: str
    suggestion: Optional[str] = None

class AlertResponse(BaseModel):
    id: int
    user_id: int
    type: str
    severity: str
    message: str
    suggestion: Optional[str]
    active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class AlertUpdate(BaseModel):
    active: Optional[bool] = None
    user_action: Optional[str] = None
