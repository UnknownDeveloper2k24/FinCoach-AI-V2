from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/coach", tags=["coach"])

@router.get("/advice")
def get_coach_advice(db: Session = Depends(get_db)):
    return {"advice": "Start saving for your goals!"}

@router.post("/chat")
def chat_with_coach(message: str, db: Session = Depends(get_db)):
    return {"response": "I'm here to help with your finances!"}
