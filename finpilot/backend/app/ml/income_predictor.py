"""
Income Prediction Engine
Predicts user income for next 7 days, 30 days with confidence scoring
"""
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import statistics

class IncomePredictor:
    def __init__(self):
        self.min_history_days = 30
        
    def predict_income(self, transactions: List[Dict], days_ahead: int = 7) -> Dict:
        """
        Predict income for next N days
        
        Args:
            transactions: List of transaction dicts with date, amount, type
            days_ahead: Number of days to predict (7 or 30)
            
        Returns:
            Dict with predictions, confidence, trend, breakdown
        """
        # Filter income transactions
        income_txns = [t for t in transactions if t.get('type') == 'income']
        
        if len(income_txns) < 5:
            return self._low_confidence_prediction(days_ahead)
        
        # Extract amounts and dates
        amounts = [t['amount'] for t in income_txns]
        dates = [t['date'] for t in income_txns]
        
        # Calculate statistics
        avg_income = statistics.mean(amounts)
        std_dev = statistics.stdev(amounts) if len(amounts) > 1 else 0
        
        # Detect trend
        recent_avg = statistics.mean(amounts[-5:]) if len(amounts) >= 5 else avg_income
        older_avg = statistics.mean(amounts[:5]) if len(amounts) >= 5 else avg_income
        
        if recent_avg > older_avg * 1.1:
            trend = "increasing"
            trend_multiplier = 1.05
        elif recent_avg < older_avg * 0.9:
            trend = "decreasing"
            trend_multiplier = 0.95
        else:
            trend = "stable"
            trend_multiplier = 1.0
        
        # Calculate confidence
        confidence = min(0.95, 0.5 + (len(amounts) / 100))
        
        # Generate daily breakdown
        predicted_amount = avg_income * trend_multiplier
        daily_predictions = []
        
        for i in range(days_ahead):
            day_date = datetime.now() + timedelta(days=i+1)
            # Add some randomness based on std dev
            daily_amount = max(0, predicted_amount + np.random.normal(0, std_dev * 0.1))
            daily_predictions.append({
                "day": day_date.strftime("%Y-%m-%d"),
                "predicted": round(daily_amount, 2)
            })
        
        total_predicted = sum(p["predicted"] for p in daily_predictions)
        
        return {
            "period": f"{days_ahead} days",
            "predicted_amount": round(total_predicted, 2),
            "confidence": round(confidence, 2),
            "trend": trend,
            "average_daily": round(predicted_amount, 2),
            "breakdown": daily_predictions,
            "historical_avg": round(avg_income, 2),
            "std_deviation": round(std_dev, 2)
        }
    
    def _low_confidence_prediction(self, days_ahead: int) -> Dict:
        """Return low confidence prediction when insufficient data"""
        return {
            "period": f"{days_ahead} days",
            "predicted_amount": 0,
            "confidence": 0.2,
            "trend": "unknown",
            "average_daily": 0,
            "breakdown": [],
            "message": "Insufficient transaction history. Add more transactions for better predictions."
        }


class ExpensePredictor:
    def __init__(self):
        pass
    
    def predict_expenses(self, transactions: List[Dict], days_ahead: int = 7) -> Dict:
        """
        Predict expenses by category for next N days
        """
        expense_txns = [t for t in transactions if t.get('type') == 'expense']
        
        if len(expense_txns) < 5:
            return {"message": "Insufficient data", "confidence": 0.2}
        
        # Group by category
        categories = {}
        for txn in expense_txns:
            cat = txn.get('category', 'Other')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(txn['amount'])
        
        # Calculate predictions per category
        predictions = []
        total_predicted = 0
        
        for category, amounts in categories.items():
            avg = statistics.mean(amounts)
            daily_avg = avg / 30  # Assume monthly average
            predicted = daily_avg * days_ahead
            
            predictions.append({
                "category": category,
                "predicted_amount": round(predicted, 2),
                "daily_average": round(daily_avg, 2),
                "historical_average": round(avg, 2)
            })
            total_predicted += predicted
        
        # Sort by amount
        predictions.sort(key=lambda x: x['predicted_amount'], reverse=True)
        
        return {
            "period": f"{days_ahead} days",
            "total_predicted": round(total_predicted, 2),
            "confidence": 0.75,
            "by_category": predictions
        }
