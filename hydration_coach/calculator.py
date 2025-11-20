# This file contains functions used to calculate daily water need.
# Algorithm idea:
# Input weight
# Process: multiply weight by 35 ml
# Output: daily water requirement
def calculate_water_requirement(weight_kg):
    """
    Calculates daily water requirement based on weight/
    Formula: 35 ml per kg of body weight
    """
    water_ml=weight_kg*35
    return water_ml
def compare_with_goal(actual_intake,goal):
    """Compares user intake with goal and returns a message."""
    if actual_intake>=goal:
        return "Great! You reached your hydration goal!"
    else:
        return "Keep drinking water to reach your goal!"
    

