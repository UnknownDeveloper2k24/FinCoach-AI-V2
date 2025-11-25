from typing import Dict, List

def classify_intent(query: str) -> str:
    """Classify user query intent"""
    query_lower = query.lower()
    
    if any(word in query_lower for word in ["afford", "can i", "should i", "spend"]):
        return "affordability"
    elif any(word in query_lower for word in ["balance", "how much", "money left"]):
        return "balance"
    elif any(word in query_lower for word in ["predict", "forecast", "earn", "income"]):
        return "income_prediction"
    elif any(word in query_lower for word in ["spending", "patterns", "overspend"]):
        return "spending_analysis"
    elif any(word in query_lower for word in ["goal", "save for", "afford"]):
        return "goal_planning"
    else:
        return "general"

def generate_coach_response(query: str, user_context: Dict) -> Dict:
    """Generate AI coach response"""
    intent = classify_intent(query)
    
    responses = {
        "affordability": {
            "answer": f"Based on your safe-to-spend limit of ₹{user_context.get('safe_to_spend', 0):.0f}, you can afford this purchase.",
            "data": {"safe_to_spend": user_context.get('safe_to_spend', 0)},
            "follow_ups": ["Check your jars", "View spending patterns"]
        },
        "balance": {
            "answer": f"Your current balance is ₹{user_context.get('balance', 0):.0f}. You can safely spend ₹{user_context.get('safe_to_spend', 0):.0f} today.",
            "data": {"balance": user_context.get('balance', 0), "safe_to_spend": user_context.get('safe_to_spend', 0)},
            "follow_ups": ["View jars", "Check predictions"]
        },
        "income_prediction": {
            "answer": f"Your predicted income for next week is ₹{user_context.get('predicted_income', 0):.0f} with {user_context.get('confidence', 0):.0%} confidence.",
            "data": user_context.get('income_prediction', {}),
            "follow_ups": ["View monthly forecast", "Check spending patterns"]
        },
        "spending_analysis": {
            "answer": "Your top spending categories are Food & Dining and Transport. Consider reducing discretionary spending.",
            "data": user_context.get('patterns', {}),
            "follow_ups": ["View optimization suggestions", "Set budget limits"]
        },
        "goal_planning": {
            "answer": "To reach your goal, you need to save ₹500/day. This is feasible based on your income.",
            "data": {"monthly_savings_needed": 15000, "feasible": True},
            "follow_ups": ["Adjust deadline", "View savings plan"]
        },
        "general": {
            "answer": "I'm here to help you manage your finances. Ask me about your balance, income predictions, or spending patterns.",
            "data": {},
            "follow_ups": ["Check balance", "View predictions", "Analyze spending"]
        }
    }
    
    return responses.get(intent, responses["general"])
