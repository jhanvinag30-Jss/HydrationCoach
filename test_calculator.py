# test_calculator.py

from hydration_coach.calculator import calculate_water, liters_and_ml

print("--- Calculator Tests ---")
print("Water for 40kg:", calculate_water(40))
print("Water for 60kg:", calculate_water(60))
print("Liters & ml for 60kg:", liters_and_ml(60))