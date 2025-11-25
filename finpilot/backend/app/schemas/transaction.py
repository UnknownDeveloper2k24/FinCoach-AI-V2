from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionCreate(BaseModel):
    date: datetime
    amount: float
    type: str  # 'income' or 'expense'
    category: Optional[str] = None
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    date: datetime
    amount: float
    type: str
    category: Optional[str]
    description: Optional[str]
    auto_categorized: bool
    confidence: float
    created_at: datetime
    
    class Config:
        from_attributes = True

class TransactionUpdate(BaseModel):
    category: Optional[str] = None
    description: Optional[str] = None
