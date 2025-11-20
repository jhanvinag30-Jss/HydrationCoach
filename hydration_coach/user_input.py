"""
Handles safe input reading for the HydrationCoach program.
"""

def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight <= 0:
                print("Weight must be positive.")
                continue
            return weight
        except ValueError:
            print("Invalid input. Please enter a number.")
