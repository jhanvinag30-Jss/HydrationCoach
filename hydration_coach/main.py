"""
Main entry point for HydrationCoach.
"""

from .calculator import recommended_ml, recommended_liters
from .reminders import generate_reminders
from .user_input import get_weight
from .config import DEFAULT_INTERVAL_ML


def main():
    print("\n=== HYDRATION COACH ===\n")

    weight = get_weight()
    daily_ml = recommended_ml(weight)
    daily_liters = recommended_liters(weight)

    print(f"\nRecommended Daily Water Intake: {daily_ml} ml ({daily_liters} liters)\n")

    print("Your hourly reminders:")
    reminders = generate_reminders(daily_ml, DEFAULT_INTERVAL_ML)

    for hour, amount in reminders:
        print(f"At {hour}:00 → Drink {amount} ml")

    print("\nStay hydrated! 💧")


if _name_ == "_main_":
    main()
