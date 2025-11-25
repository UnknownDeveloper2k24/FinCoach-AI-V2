from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Jar(Base):
    __tablename__ = "jars"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)
    target_amount = Column(Float, default=0)
    current_amount = Column(Float, default=0)
    priority = Column(Integer, default=1)
    deadline = Column(DateTime)
    color = Column(String(20), default="bg-blue-500")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="jars")
