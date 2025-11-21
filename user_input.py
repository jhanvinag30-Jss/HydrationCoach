# user_input.py
# Provides user information for the hydration program.

def get_user():
    """
    Simulates user data.
    Demonstrates dictionary, keys, conditionals.
    """

    user = {
        "name": "Demo User",
        "weight": 55,
        "interval": 200
    }

    # Validation
    if user["weight"] <= 0:
        user["weight"] = 50

    return user