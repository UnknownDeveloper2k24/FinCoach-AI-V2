from datetime import datetime, timedelta
from typing import Dict, List, Optional

def predict_cash_runout(current_balance: float, daily_expense_avg: float, predicted_income: float) -> Optional[Dict]:
    """Predict when user might run out of money"""
    
    if daily_expense_avg <= 0:
        return None
    
    # Monthly burn rate
    monthly_burn = daily_expense_avg * 30
    
    if predicted_income >= monthly_burn:
        return None  # No runout risk
    
    net_daily_burn = daily_expense_avg - (predicted_income / 30)
    
    if net_daily_burn <= 0:
        return None
    
    days_until_runout = current_balance / net_daily_burn
    
    if days_until_runout < 0:
        days_until_runout = 0
    
    runout_date = datetime.now() + timedelta(days=days_until_runout)
    
    # Confidence based on data consistency
    confidence = min(0.95, 0.7 + (min(days_until_runout, 30) / 30) * 0.25)
    
    return {
        "days_until_runout": round(days_until_runout, 1),
        "runout_date": runout_date.strftime("%Y-%m-%d"),
        "confidence": round(confidence, 2),
        "risk_level": "critical" if days_until_runout < 7 else "warning" if days_until_runout < 14 else "info"
    }

def calculate_safe_to_spend(current_balance: float, daily_expense_avg: float, days_ahead: int = 7) -> float:
    """Calculate safe daily spending limit"""
    
    if days_ahead <= 0:
        return 0
    
    # Reserve 30% for emergencies
    available = current_balance * 0.7
    safe_daily = available / days_ahead
    
    return round(max(0, safe_daily), 2)
