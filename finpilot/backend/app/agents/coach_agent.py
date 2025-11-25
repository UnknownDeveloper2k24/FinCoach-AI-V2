"""
Multi-Agent AI Coach System
Routes queries to specialized agents for financial advice
"""
import re
from typing import Dict, List, Optional
from datetime import datetime

class IntentClassifier:
    """Classifies user queries into intents"""
    
    def classify(self, query: str) -> str:
        """
        Classify query intent
        Returns: income_prediction, spending_analysis, goal_planning, affordability, balance, general
        """
        query_lower = query.lower()
        
        # Income prediction keywords
        if any(word in query_lower for word in ['predict', 'forecast', 'earn', 'income', 'next week', 'next month', 'how much will']):
            return "income_prediction"
        
        # Spending analysis keywords
        if any(word in query_lower for word in ['spending', 'patterns', 'overspend', 'categories', 'where do i', 'analysis']):
            return "spending_analysis"
        
        # Goal planning keywords
        if any(word in query_lower for word in ['afford', 'save for', 'goal', 'buy', 'can i', 'feasible']):
            return "goal_planning"
        
        # Affordability keywords
        if any(word in query_lower for word in ['can i afford', 'should i spend', 'is it okay', 'can i buy']):
            return "affordability"
        
        # Balance keywords
        if any(word in query_lower for word in ['balance', 'how much', 'money left', 'current balance', 'jars']):
            return "balance"
        
        return "general"


class IncomeAgent:
    """Handles income prediction queries"""
    
    def handle(self, query: str, user_context: Dict) -> Dict:
        """Handle income prediction query"""
        predicted_income = user_context.get('predicted_income', {})
        
        return {
            "type": "income_prediction",
            "answer": f"Based on your transaction history, your predicted income for the next 7 days is ₹{predicted_income.get('predicted_amount', 0):.0f} with {predicted_income.get('confidence', 0)*100:.0f}% confidence. Your income trend is {predicted_income.get('trend', 'stable')}.",
            "data": predicted_income,
            "follow_ups": [
                "What's my monthly income forecast?",
                "How confident are you about this prediction?",
                "What factors affect my income?"
            ]
        }


class SpendingAgent:
    """Handles spending analysis queries"""
    
    def handle(self, query: str, user_context: Dict) -> Dict:
        """Handle spending analysis query"""
        patterns = user_context.get('spending_patterns', {})
        top_categories = patterns.get('patterns', [])[:3]
        
        category_text = ", ".join([f"₹{cat['average_amount']:.0f} on {cat['category']}" for cat in top_categories])
        
        return {
            "type": "spending_analysis",
            "answer": f"Your top spending categories are: {category_text}. You're spending the most on {top_categories[0]['category'] if top_categories else 'various categories'}. Would you like suggestions to reduce spending?",
            "data": patterns,
            "follow_ups": [
                "How can I reduce spending?",
                "What are my anomalies?",
                "Show me recurring transactions"
            ]
        }


class GoalAgent:
    """Handles goal planning queries"""
    
    def handle(self, query: str, user_context: Dict) -> Dict:
        """Handle goal planning query"""
        # Extract amount from query if present
        amount_match = re.search(r'₹?(\d+(?:,\d+)*(?:\.\d+)?)', query)
        amount = float(amount_match.group(1).replace(',', '')) if amount_match else 0
        
        predicted_income = user_context.get('predicted_income', {}).get('predicted_amount', 0)
        monthly_income = predicted_income * 4.3  # Approximate monthly
        
        if amount > 0:
            months_needed = amount / (monthly_income * 0.2)  # Assume 20% savings rate
            answer = f"To save ₹{amount:.0f}, you'd need approximately {months_needed:.1f} months at your current income level. This is {'feasible' if months_needed < 12 else 'challenging'}."
        else:
            answer = "To help you plan a goal, please tell me the amount you want to save and the deadline."
        
        return {
            "type": "goal_planning",
            "answer": answer,
            "data": {"amount": amount, "months_needed": months_needed if amount > 0 else 0},
            "follow_ups": [
                "Help me create a savings plan",
                "Can I reach this goal?",
                "What should I cut to save more?"
            ]
        }


class AffordabilityAgent:
    """Handles affordability queries"""
    
    def handle(self, query: str, user_context: Dict) -> Dict:
        """Handle affordability query"""
        # Extract amount from query
        amount_match = re.search(r'₹?(\d+(?:,\d+)*(?:\.\d+)?)', query)
        amount = float(amount_match.group(1).replace(',', '')) if amount_match else 0
        
        safe_to_spend = user_context.get('safe_to_spend', 0)
        balance = user_context.get('balance', 0)
        
        if amount <= 0:
            return {
                "type": "affordability",
                "answer": "Please tell me the amount you want to spend, and I'll let you know if it's affordable.",
                "data": {},
                "follow_ups": []
            }
        
        if amount <= safe_to_spend:
            answer = f"Yes, you can afford ₹{amount:.0f}! Your safe daily spending limit is ₹{safe_to_spend:.0f}."
            affordable = True
        else:
            shortfall = amount - safe_to_spend
            answer = f"This might be tight. You can safely spend ₹{safe_to_spend:.0f}, but you're asking for ₹{amount:.0f}. You'd be ₹{shortfall:.0f} short."
            affordable = False
        
        return {
            "type": "affordability",
            "answer": answer,
            "data": {"amount": amount, "safe_to_spend": safe_to_spend, "affordable": affordable},
            "follow_ups": [
                "What's my safe spending limit?",
                "How can I afford this?",
                "Show me my jars"
            ]
        }


class BalanceAgent:
    """Handles balance and status queries"""
    
    def handle(self, query: str, user_context: Dict) -> Dict:
        """Handle balance query"""
        balance = user_context.get('balance', 0)
        safe_to_spend = user_context.get('safe_to_spend', 0)
        jars = user_context.get('jars', [])
        
        jar_text = ", ".join([f"{jar['name']}: ₹{jar['current']:.0f}/{jar['target']:.0f}" for jar in jars[:3]])
        
        return {
            "type": "balance",
            "answer": f"Your current balance is ₹{balance:.0f}. You can safely spend ₹{safe_to_spend:.0f} today. Your jars: {jar_text}.",
            "data": {"balance": balance, "safe_to_spend": safe_to_spend, "jars": jars},
            "follow_ups": [
                "Show me my jars",
                "What's my safe spending limit?",
                "How much can I save?"
            ]
        }


class GeneralAgent:
    """Handles general financial advice"""
    
    def handle(self, query: str, user_context: Dict) -> Dict:
        """Handle general query"""
        return {
            "type": "general",
            "answer": "I can help you with income predictions, spending analysis, goal planning, affordability checks, and balance inquiries. What would you like to know?",
            "data": {},
            "follow_ups": [
                "Predict my income",
                "Analyze my spending",
                "Help me save for a goal",
                "Can I afford this?"
            ]
        }


class CoachRouter:
    """Routes queries to appropriate agents"""
    
    def __init__(self):
        self.classifier = IntentClassifier()
        self.agents = {
            "income_prediction": IncomeAgent(),
            "spending_analysis": SpendingAgent(),
            "goal_planning": GoalAgent(),
            "affordability": AffordabilityAgent(),
            "balance": BalanceAgent(),
            "general": GeneralAgent()
        }
    
    def route(self, query: str, user_context: Dict) -> Dict:
        """Route query to appropriate agent"""
        intent = self.classifier.classify(query)
        agent = self.agents.get(intent, self.agents["general"])
        
        response = agent.handle(query, user_context)
        response["intent"] = intent
        response["timestamp"] = datetime.now().isoformat()
        
        return response
