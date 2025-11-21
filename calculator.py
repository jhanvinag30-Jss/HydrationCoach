# calculator.py
# Contains functions for calculating daily water intake.

from config import DAILY_MULTIPLIER

def calculate_water(weight):
    """
    Returns daily water requirement in milliliters.
    Formula: weight * DAILY_MULTIPLIER
    """
    return weight * DAILY_MULTIPLIER


def liters_and_ml(weight):
    """
    Converts ml to liters + remaining ml.
    """
    total_ml = calculate_water(weight)
    liters = total_ml // 1000
    ml_remaining = total_ml % 1000
    return liters, ml_remaining