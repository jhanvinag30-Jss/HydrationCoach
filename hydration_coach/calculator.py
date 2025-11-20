"""
Contains functions to calculate water intake recommendations.
"""

from .config import MIN_WATER_ML, ML_PER_KG


def recommended_ml(weight_kg: float) -> int:
    """
    Returns the recommended water intake in ml based on body weight.
    """
    calculated = int(weight_kg * ML_PER_KG)
    return max(calculated, MIN_WATER_ML)


def recommended_liters(weight_kg: float) -> float:
    """
    Converts water intake from ml to liters.
    """
    return round(recommended_ml(weight_kg) / 1000, 2)
