from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.database import engine, Base
from app.models import User, Transaction, Jar, Goal, Alert, UserInteraction, Prediction
from app.api import auth, transactions, jars, goals, predictions, alerts, insights, coach, sms_parser

settings = get_settings()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinPilot API",
    version="2.0.0",
    description="AI-powered financial OS for gig workers with advanced ML and multi-agent coaching"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(transactions.router)
app.include_router(jars.router)
app.include_router(goals.router)
app.include_router(predictions.router)
app.include_router(alerts.router)
app.include_router(insights.router)
app.include_router(coach.router)
app.include_router(sms_parser.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FinPilot API is running"}

@app.get("/")
def root():
    return {
        "message": "Welcome to FinPilot API v2.0",
        "docs": "/docs",
        "version": "2.0.0",
        "features": [
            "Multi-agent AI Coach",
            "Income & Expense Predictions",
            "Spending Pattern Analysis",
            "Budget Optimization",
            "SMS Parser (5 Indian Banks)",
            "Cashflow Analysis",
            "Goal Planning",
            "Smart Jars",
            "Proactive Alerts"
        ]
    }
