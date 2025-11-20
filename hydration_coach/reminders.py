"""
Generates water-drinking reminders for the day.
"""

def generate_reminders(total_ml: int, interval_ml: int):
    """
    Creates reminders in (hour, amount) format.
    Water reminders occur hourly until daily goal is reached.
    """

    reminders = []
    remaining = total_ml
    hour = 8  # start at 8 AM

    while remaining > 0 and hour <= 22:
        drink_amount = min(interval_ml, remaining)
        reminders.append((hour, drink_amount))
        remaining -= drink_amount
        hour += 1

    return reminders
