from app.agents.coach import classify_intent, generate_coach_response

def route_query(query: str, user_context: dict) -> dict:
    """Route user query to appropriate agent"""
    intent = classify_intent(query)
    response = generate_coach_response(query, user_context)
    return {
        "intent": intent,
        "response": response
    }
