"""
Budget Optimizer
Generates prioritized optimization suggestions based on spending patterns
"""
import statistics
from typing import Dict, List

class BudgetOptimizer:
    def __init__(self):
        pass
    
    def optimize_budget(self, transactions: List[Dict], predicted_income: float) -> Dict:
        """
        Analyze spending inefficiencies and generate optimization suggestions
        """
        expense_txns = [t for t in transactions if t.get('type') == 'expense']
        
        if len(expense_txns) < 5:
            return {"message": "Insufficient data", "optimizations": []}
        
        # Group by category
        categories = {}
        for txn in expense_txns:
            cat = txn.get('category', 'Other')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(txn['amount'])
        
        # Calculate current spending
        total_spending = sum(sum(amounts) for amounts in categories.values())
        daily_spending = total_spending / 30  # Assume monthly average
        
        # Generate optimization suggestions
        optimizations = []
        total_potential_savings = 0
        
        for category, amounts in categories.items():
            avg_spending = statistics.mean(amounts)
            monthly_spending = avg_spending * len(amounts) / max(1, len(expense_txns)) * 30
            
            # Suggest 20-30% reduction for discretionary categories
            if category in ['Food & Dining', 'Entertainment', 'Shopping & Retail', 'Personal Care']:
                suggested_reduction = 0.25
                priority = "high"
            elif category in ['Transport & Fuel', 'Bills & Utilities']:
                suggested_reduction = 0.15
                priority = "medium"
            else:
                suggested_reduction = 0.10
                priority = "low"
            
            potential_savings = monthly_spending * suggested_reduction
            
            if potential_savings > 100:  # Only suggest if savings > ₹100
                optimizations.append({
                    "priority": priority,
                    "category": category,
                    "current_spending": round(monthly_spending, 2),
                    "suggested_spending": round(monthly_spending * (1 - suggested_reduction), 2),
                    "potential_savings": round(potential_savings, 2),
                    "action": f"Reduce {category} by {int(suggested_reduction * 100)}%",
                    "reason": f"You're spending ₹{monthly_spending:.0f}/month on {category}"
                })
                total_potential_savings += potential_savings
        
        # Sort by priority and savings
        priority_order = {"high": 0, "medium": 1, "low": 2}
        optimizations.sort(key=lambda x: (priority_order[x['priority']], -x['potential_savings']))
        
        # Calculate optimized daily limit
        optimized_daily_limit = (predicted_income / 30) * 0.7  # 70% of daily income
        
        return {
            "optimizations": optimizations[:5],  # Top 5 suggestions
            "total_potential_savings": round(total_potential_savings, 2),
            "current_daily_spending": round(daily_spending, 2),
            "optimized_daily_limit": round(optimized_daily_limit, 2),
            "reasoning": f"Based on your predicted income of ₹{predicted_income:.0f}, you can safely spend ₹{optimized_daily_limit:.0f}/day"
        }
    
    def calculate_safe_to_spend(self, balance: float, predicted_income: float, 
                               jar_targets: Dict[str, float], days_until_deadline: Dict[str, int]) -> float:
        """
        Calculate safe daily spending limit
        """
        # Calculate jar shortfalls
        total_shortfall = sum(max(0, target - 0) for target in jar_targets.values())
        
        # Calculate days until nearest deadline
        min_days = min(days_until_deadline.values()) if days_until_deadline else 30
        
        # Daily allocation needed for jars
        daily_jar_allocation = total_shortfall / max(1, min_days)
        
        # Safe to spend = (balance + predicted_income - jar_allocation) / days
        safe_daily = max(0, (balance + predicted_income - daily_jar_allocation) / 30)
        
        return round(safe_daily, 2)


class CashflowAnalyzer:
    def __init__(self):
        pass
    
    def predict_cash_runout(self, balance: float, daily_expense_avg: float, 
                           predicted_income: float) -> Dict:
        """
        Predict when user might run out of money
        """
        if predicted_income >= daily_expense_avg * 30:
            return {
                "risk": "low",
                "days_until_runout": None,
                "message": "No cash runout risk detected"
            }
        
        # Calculate net daily burn
        net_daily_burn = daily_expense_avg - (predicted_income / 30)
        
        if net_daily_burn <= 0:
            return {
                "risk": "low",
                "days_until_runout": None,
                "message": "Income covers expenses"
            }
        
        # Calculate days until runout
        days_until_runout = balance / net_daily_burn
        
        if days_until_runout < 0:
            risk = "critical"
        elif days_until_runout < 7:
            risk = "critical"
        elif days_until_runout < 14:
            risk = "high"
        elif days_until_runout < 30:
            risk = "medium"
        else:
            risk = "low"
        
        from datetime import datetime, timedelta
        runout_date = (datetime.now() + timedelta(days=days_until_runout)).strftime("%Y-%m-%d")
        
        return {
            "risk": risk,
            "days_until_runout": round(days_until_runout, 1),
            "runout_date": runout_date,
            "daily_burn": round(net_daily_burn, 2),
            "confidence": 0.75,
            "suggestion": f"Reduce daily spending to ₹{(predicted_income/30):.0f} or increase income"
        }
