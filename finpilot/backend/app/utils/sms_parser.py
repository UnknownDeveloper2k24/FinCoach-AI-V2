"""
UPI SMS Parser for Indian Banks
Parses SMS from 5 major Indian banks and auto-categorizes transactions
"""
import re
from typing import Dict, Optional

class SMSParser:
    """Parse UPI SMS from Indian banks"""
    
    # SMS patterns for 5 major Indian banks
    SMS_PATTERNS = [
        # HDFC Bank
        {
            "bank": "HDFC",
            "debit_pattern": r"Rs\.(\d+(?:,\d+)*(?:\.\d+)?)\s+debited.*?to\s+(.+?)\s+on",
            "credit_pattern": r"Rs\.(\d+(?:,\d+)*(?:\.\d+)?)\s+credited.*?from\s+(.+?)\s+on",
        },
        # ICICI Bank
        {
            "bank": "ICICI",
            "debit_pattern": r"INR\s+(\d+(?:,\d+)*(?:\.\d+)?)\s+debited.*?at\s+(.+?)\.",
            "credit_pattern": r"INR\s+(\d+(?:,\d+)*(?:\.\d+)?)\s+credited.*?from\s+(.+?)\.",
        },
        # SBI (State Bank of India)
        {
            "bank": "SBI",
            "debit_pattern": r"Rs\s+(\d+(?:,\d+)*(?:\.\d+)?)\s+debited.*?to\s+(.+?)\s+on",
            "credit_pattern": r"Rs\s+(\d+(?:,\d+)*(?:\.\d+)?)\s+credited.*?from\s+(.+?)\s+on",
        },
        # Axis Bank
        {
            "bank": "Axis",
            "debit_pattern": r"Rs\s+(\d+(?:,\d+)*(?:\.\d+)?)\s+debited.*?at\s+(.+?)\.",
            "credit_pattern": r"Rs\s+(\d+(?:,\d+)*(?:\.\d+)?)\s+credited.*?from\s+(.+?)\.",
        },
        # Kotak Mahindra Bank
        {
            "bank": "Kotak",
            "debit_pattern": r"Rs\.(\d+(?:,\d+)*(?:\.\d+)?)\s+debited.*?to\s+(.+?)\s+on",
            "credit_pattern": r"Rs\.(\d+(?:,\d+)*(?:\.\d+)?)\s+credited.*?from\s+(.+?)\s+on",
        },
    ]
    
    # Category detection rules
    CATEGORY_RULES = {
        "Food & Dining": ["zomato", "swiggy", "food", "restaurant", "cafe", "pizza", "burger", "biryani"],
        "Transport & Fuel": ["uber", "ola", "petrol", "fuel", "gas", "taxi", "auto", "metro"],
        "Bills & Utilities": ["electricity", "water", "gas", "internet", "phone", "bill"],
        "Rent & Housing": ["rent", "lease", "landlord", "property"],
        "Shopping & Retail": ["amazon", "flipkart", "shop", "store", "mall", "retail"],
        "Entertainment": ["movie", "cinema", "netflix", "spotify", "game", "entertainment"],
        "Healthcare": ["hospital", "doctor", "pharmacy", "medical", "health"],
        "Education": ["school", "college", "course", "tuition", "education"],
        "Savings & Investment": ["investment", "mutual", "stock", "savings"],
        "EMI & Loans": ["emi", "loan", "credit", "installment"],
        "Personal Care": ["salon", "gym", "spa", "beauty"],
        "Other": []
    }
    
    def parse_sms(self, sms_text: str) -> Dict:
        """
        Parse SMS and extract transaction details
        
        Args:
            sms_text: Raw SMS text from bank
            
        Returns:
            Dict with parsed transaction details
        """
        sms_lower = sms_text.lower()
        
        # Try each bank pattern
        for pattern_config in self.SMS_PATTERNS:
            bank = pattern_config["bank"]
            
            # Try debit pattern
            debit_match = re.search(pattern_config["debit_pattern"], sms_text, re.IGNORECASE)
            if debit_match:
                amount_str = debit_match.group(1)
                merchant = debit_match.group(2)
                
                amount = float(amount_str.replace(',', ''))
                category = self._detect_category(merchant)
                
                return {
                    "parsed_successfully": True,
                    "amount": amount,
                    "type": "expense",
                    "merchant": merchant.strip(),
                    "category": category["category"],
                    "confidence": category["confidence"],
                    "bank": bank,
                    "raw_sms": sms_text
                }
            
            # Try credit pattern
            credit_match = re.search(pattern_config["credit_pattern"], sms_text, re.IGNORECASE)
            if credit_match:
                amount_str = credit_match.group(1)
                merchant = credit_match.group(2)
                
                amount = float(amount_str.replace(',', ''))
                category = self._detect_category(merchant)
                
                return {
                    "parsed_successfully": True,
                    "amount": amount,
                    "type": "income",
                    "merchant": merchant.strip(),
                    "category": category["category"],
                    "confidence": category["confidence"],
                    "bank": bank,
                    "raw_sms": sms_text
                }
        
        return {
            "parsed_successfully": False,
            "error": "Could not parse SMS. Please check the format.",
            "raw_sms": sms_text
        }
    
    def _detect_category(self, merchant: str) -> Dict:
        """
        Detect transaction category from merchant name
        
        Returns:
            Dict with category and confidence score
        """
        merchant_lower = merchant.lower()
        
        for category, keywords in self.CATEGORY_RULES.items():
            if category == "Other":
                continue
            
            for keyword in keywords:
                if keyword in merchant_lower:
                    return {
                        "category": category,
                        "confidence": 0.9 if len(keyword) > 3 else 0.7
                    }
        
        return {
            "category": "Other",
            "confidence": 0.5
        }
    
    def parse_bulk_sms(self, sms_list: list) -> list:
        """
        Parse multiple SMS messages
        
        Args:
            sms_list: List of SMS texts
            
        Returns:
            List of parsed transactions
        """
        results = []
        for sms in sms_list:
            result = self.parse_sms(sms)
            results.append(result)
        
        return results
