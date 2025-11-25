from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/alerts", tags=["alerts"])

@router.get("/")
def get_alerts(db: Session = Depends(get_db)):
    return {"alerts": []}

@router.post("/mark-read/{alert_id}")
def mark_alert_read(alert_id: int, db: Session = Depends(get_db)):
    return {"message": "Alert marked as read"}
