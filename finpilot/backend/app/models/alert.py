from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50), nullable=False)
    severity = Column(String(20), default="info")
    message = Column(String(500))
    suggestion = Column(String(500))
    active = Column(Boolean, default=True)
    dismissed_at = Column(DateTime)
    user_action = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="alerts")
    interactions = relationship("UserInteraction", back_populates="alert")
