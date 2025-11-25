from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/api/jars", tags=["jars"])

class Jar(BaseModel):
    name: str
    goal_amount: float

@router.get("/")
def get_jars(db: Session = Depends(get_db)):
    return {"jars": []}

@router.post("/")
def create_jar(jar: Jar, db: Session = Depends(get_db)):
    return {"message": "Jar created", "data": jar}
