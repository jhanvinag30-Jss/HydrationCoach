from calculator import calculate_water, liters_and_ml
from reminders import generate_reminders
from user_input import get_user

def main():
    # Get user dictionary
    user = get_user()

    # Extract values safely
    name = user["name"]
    weight = user["weight"]
    interval = user["interval"]

    # Calculate hydration needs
    liters, ml = liters_and_ml(weight)

    print("--- HYDRATION COACH OUTPUT ---")
    print(f"User: {name}")
    print(f"Weight: {weight} kg")
    print(f"Daily Recommended Intake: {ml} ml ({liters} liters)")

    # Generate reminders
    reminders = generate_reminders(ml, interval)

    print("Reminder Schedule:")
    for hour, amount in reminders:
        print(f" {hour}:00 -> {amount} ml")

# Always required for Python scripts
if __name__ == "__main__":
    main()