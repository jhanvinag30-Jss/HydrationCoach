"""
user_input.py
Simulated user input for testing.
Shows dictionary and conditionals.
"""

def get_user():
    user = {
        "name": "Demo User",
        "weight": 55,
        "interval": 250
    }

    # Simple validation
    if user["weight"] <= 0:
        user["weight"] = 50  # default safe fallback

    return user
