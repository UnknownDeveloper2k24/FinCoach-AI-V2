from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/insights", tags=["insights"])

@router.get("/spending-patterns")
def get_spending_patterns(db: Session = Depends(get_db)):
    return {"patterns": []}

@router.get("/budget-analysis")
def get_budget_analysis(db: Session = Depends(get_db)):
    return {"analysis": {}}
