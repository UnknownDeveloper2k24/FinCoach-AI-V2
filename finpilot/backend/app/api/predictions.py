from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/predictions", tags=["predictions"])

@router.get("/income")
def get_income_prediction(db: Session = Depends(get_db)):
    return {"prediction": 50000, "confidence": 0.85}

@router.get("/expenses")
def get_expense_prediction(db: Session = Depends(get_db)):
    return {"prediction": 15000, "confidence": 0.80}
