from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from pydantic import BaseModel

router = APIRouter(prefix="/api/auth", tags=["auth"])

class UserRegister(BaseModel):
    email: str
    name: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    return {"message": "User registered successfully", "email": user.email}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return {"message": "Login successful", "token": "sample_token"}

@router.get("/me")
def get_current_user():
    return {"id": 1, "email": "user@example.com", "name": "User"}
