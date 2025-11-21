"""
calculator.py
Contains functions that calculate recommended water intake.
Includes algorithm explanation, conditionals, tuple assignment.
"""

from config import ML_PER_KG, MIN_WATER_ML

def calculate_water(weight_kg):
    """
    Algorithm (Top-down):
    1. Multiply weight × ML_PER_KG
    2. Ensure the value is not below MIN_WATER_ML (conditional)
    3. Return the final result

    Example flow:
    weight = 50 → 50*35 = 1750 ml → return 1750
    """
    if weight_kg <= 0:
        return "Invalid weight. Must be positive."

    calculated = weight_kg * ML_PER_KG

    # Use of precedence: multiplication happens before comparison
    final_value = calculated if calculated >= MIN_WATER_ML else MIN_WATER_ML
    return final_value


def liters_and_ml(weight):
    """
    Returns a tuple (liters, ml) using tuple assignment.
    """
    ml = calculate_water(weight)

    if isinstance(ml, str):  
        return (0, ml)       # error message in tuple second position

    liters = round(ml / 1000, 2)
    return (liters, ml)