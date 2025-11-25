from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/api/sms", tags=["sms"])

class SMSMessage(BaseModel):
    content: str
    sender: str

@router.post("/parse")
def parse_sms(sms: SMSMessage, db: Session = Depends(get_db)):
    return {"message": "SMS parsed successfully", "transaction": {}}
