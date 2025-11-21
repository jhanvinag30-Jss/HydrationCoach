"""
reminders.py
Generates hourly reminders based on total intake.
Demonstrates loops, list, break, continue, pass.
"""

def generate_reminders(total_ml, interval_ml=250):
    """
    Pseudo-code:
    --------------------
    SET hour = 8
    WHILE total_ml > 0:
        IF hour > 22: STOP (break)
        CREATE reminder
        REDUCE total_ml
        INCREASE hour
    RETURN list
    --------------------
    """

    reminders = []  # List to store results
    hour = 8

    while total_ml > 0:
        if hour > 22:   # Condition to stop loop early
            break

        if interval_ml <= 0:
            # continue demonstrates skipping an invalid value
            continue

        amount = min(interval_ml, total_ml)
        reminders.append((hour, amount))

        total_ml -= amount
        hour += 1

        # A pass statement — does nothing (placeholder)
        pass

    return reminders
