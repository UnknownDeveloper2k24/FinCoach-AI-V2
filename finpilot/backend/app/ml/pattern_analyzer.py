"""
Pattern Detection Engine
Detects spending patterns, anomalies, and recurring transactions
"""
import statistics
from datetime import datetime, timedelta
from typing import Dict, List
from collections import Counter

class PatternAnalyzer:
    def __init__(self):
        pass
    
    def analyze_patterns(self, transactions: List[Dict]) -> Dict:
        """
        Analyze spending patterns by category
        """
        expense_txns = [t for t in transactions if t.get('type') == 'expense']
        
        if len(expense_txns) < 5:
            return {"message": "Insufficient data", "patterns": []}
        
        # Group by category
        categories = {}
        for txn in expense_txns:
            cat = txn.get('category', 'Other')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(txn)
        
        patterns = []
        
        for category, txns in categories.items():
            amounts = [t['amount'] for t in txns]
            avg_amount = statistics.mean(amounts)
            
            # Calculate frequency
            frequency = len(txns) / max(1, (datetime.now() - datetime.fromisoformat(txns[0]['date'])).days) * 7
            
            # Find peak day
            days = [datetime.fromisoformat(t['date']).strftime("%A") for t in txns]
            peak_day = Counter(days).most_common(1)[0][0] if days else "Unknown"
            
            # Detect trend
            recent_avg = statistics.mean(amounts[-3:]) if len(amounts) >= 3 else avg_amount
            older_avg = statistics.mean(amounts[:3]) if len(amounts) >= 3 else avg_amount
            
            if recent_avg > older_avg * 1.1:
                trend = "increasing"
            elif recent_avg < older_avg * 0.9:
                trend = "decreasing"
            else:
                trend = "stable"
            
            patterns.append({
                "category": category,
                "average_amount": round(avg_amount, 2),
                "frequency": f"{frequency:.1f} times/week",
                "peak_day": peak_day,
                "trend": trend,
                "transaction_count": len(txns)
            })
        
        # Sort by amount
        patterns.sort(key=lambda x: x['average_amount'], reverse=True)
        
        # Detect anomalies
        anomalies = self._detect_anomalies(expense_txns)
        
        return {
            "patterns": patterns,
            "anomalies": anomalies,
            "total_transactions": len(expense_txns)
        }
    
    def _detect_anomalies(self, transactions: List[Dict]) -> List[Dict]:
        """
        Detect anomalous transactions (statistical outliers)
        """
        anomalies = []
        
        # Group by category
        categories = {}
        for txn in transactions:
            cat = txn.get('category', 'Other')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(txn)
        
        for category, txns in categories.items():
            amounts = [t['amount'] for t in txns]
            
            if len(amounts) < 3:
                continue
            
            avg = statistics.mean(amounts)
            std_dev = statistics.stdev(amounts)
            threshold = avg + (2 * std_dev)  # 2 std devs above mean
            
            for txn in txns:
                if txn['amount'] > threshold:
                    anomalies.append({
                        "transaction_id": txn.get('id'),
                        "amount": txn['amount'],
                        "category": category,
                        "date": txn['date'],
                        "reason": f"{txn['amount']:.0f} is {(txn['amount']/avg):.1f}x higher than category average",
                        "severity": "high" if txn['amount'] > avg * 3 else "medium"
                    })
        
        return sorted(anomalies, key=lambda x: x['amount'], reverse=True)[:5]
    
    def detect_recurring(self, transactions: List[Dict]) -> List[Dict]:
        """
        Detect recurring transactions (subscriptions, EMIs, etc.)
        """
        recurring = []
        
        # Group by merchant/description
        merchants = {}
        for txn in transactions:
            desc = txn.get('description', 'Unknown')
            if desc not in merchants:
                merchants[desc] = []
            merchants[desc].append(txn)
        
        for desc, txns in merchants.items():
            if len(txns) >= 2:
                amounts = [t['amount'] for t in txns]
                
                # Check if amounts are consistent
                if len(set(amounts)) == 1:  # All same amount
                    recurring.append({
                        "description": desc,
                        "amount": amounts[0],
                        "frequency": f"{len(txns)} times",
                        "category": txns[0].get('category', 'Other')
                    })
        
        return recurring
