from typing import Dict, List

DEFAULT_JARS = [
    {"name": "Rent", "priority": 1, "color": "bg-blue-500"},
    {"name": "Bills", "priority": 2, "color": "bg-yellow-500"},
    {"name": "Emergency", "priority": 3, "color": "bg-red-500"},
    {"name": "Savings", "priority": 4, "color": "bg-green-500"},
]

def allocate_income_to_jars(predicted_income: float, jars: List[Dict], current_balances: Dict) -> Dict:
    """Allocate predicted income to jars based on priority"""
    
    remaining_income = predicted_income
    allocations = {}
    
    # Sort by priority
    sorted_jars = sorted(jars, key=lambda x: x.get('priority', 999))
    
    for jar in sorted_jars:
        needed = jar.get('target_amount', 0) - current_balances.get(jar['name'], 0)
        
        if jar['priority'] == 1:  # Rent
            allocation = min(remaining_income * 0.5, max(0, needed))
        elif jar['priority'] == 2:  # Bills
            allocation = min(remaining_income * 0.15, max(0, needed))
        elif jar['priority'] == 3:  # Emergency
            allocation = min(remaining_income * 0.10, max(0, needed))
        else:  # Savings
            allocation = min(remaining_income, max(0, needed))
        
        allocations[jar['name']] = round(allocation, 2)
        remaining_income -= allocation
        
        if remaining_income <= 0:
            break
    
    safe_to_spend = max(0, remaining_income)
    
    return {
        "allocations": allocations,
        "safe_to_spend": round(safe_to_spend, 2)
    }
