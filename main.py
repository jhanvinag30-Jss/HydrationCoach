# main.py
# Main program for Hydration Coach.

from user_input import get_user
from calculator import calculate_water, liters_and_ml
from reminders import show_reminders

def main():
    user = get_user()
    name = user["name"]
    weight = user["weight"]

    print("---- HYDRATION COACH ----")
    print(f"User Name: {name}")
    print(f"Weight: {weight} kg")

    total_ml = calculate_water(weight)
    liters, ml_remaining = liters_and_ml(weight)

    print(f"\nDaily Water Requirement: {total_ml} ml")
    print(f"That is: {liters} liters and {ml_remaining} ml")

    print("\n--- Reminders ---")
    show_reminders(2)


if __name__ == "__main__":
    main()