from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/api/transactions", tags=["transactions"])

class Transaction(BaseModel):
    amount: float
    category: str
    description: str

@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return {"transactions": []}

@router.post("/")
def create_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    return {"message": "Transaction created", "data": transaction}
