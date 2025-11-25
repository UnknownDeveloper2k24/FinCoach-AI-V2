import re
from typing import Dict, Tuple

CATEGORY_RULES = {
    "Food & Dining": ["zomato", "swiggy", "food", "restaurant", "cafe", "pizza", "burger", "biryani"],
    "Transport & Fuel": ["uber", "ola", "petrol", "fuel", "gas", "taxi", "auto", "metro"],
    "Bills & Utilities": ["electricity", "water", "internet", "phone", "bill", "utility"],
    "Rent & Housing": ["rent", "lease", "landlord", "housing", "apartment"],
    "Shopping & Retail": ["amazon", "flipkart", "mall", "store", "shop", "retail"],
    "Entertainment": ["movie", "cinema", "netflix", "spotify", "game", "concert"],
    "Healthcare": ["doctor", "hospital", "pharmacy", "medicine", "health", "clinic"],
    "Education": ["school", "college", "course", "tuition", "book", "education"],
    "Savings & Investment": ["savings", "investment", "mutual", "stock", "deposit"],
    "EMI & Loans": ["emi", "loan", "credit", "installment", "mortgage"],
    "Personal Care": ["salon", "gym", "spa", "beauty", "haircut"],
    "Other": []
}

def detect_category(merchant: str, description: str = "") -> Tuple[str, float]:
    """Detect transaction category from merchant/description"""
    text = f"{merchant} {description}".lower()
    
    best_match = "Other"
    best_confidence = 0.0
    
    for category, keywords in CATEGORY_RULES.items():
        if category == "Other":
            continue
        
        matches = sum(1 for keyword in keywords if keyword in text)
        if matches > 0:
            confidence = min(0.95, 0.5 + (matches * 0.15))
            if confidence > best_confidence:
                best_confidence = confidence
                best_match = category
    
    return best_match, round(best_confidence, 2)

def get_category_suggestions(merchant: str) -> list:
    """Get alternative category suggestions"""
    category, conf = detect_category(merchant)
    suggestions = [cat for cat in CATEGORY_RULES.keys() if cat != category and cat != "Other"]
    return suggestions[:3]
