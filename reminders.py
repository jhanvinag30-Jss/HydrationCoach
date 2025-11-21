# reminders.py
# Shows simple water reminders using loops.

from config import REMINDER_MESSAGES

def show_reminders(count):
    """
    Prints a certain number of hydration reminders.
    Uses a loop for repeated messages.
    """
    for i in range(count):
        message = REMINDER_MESSAGES[i % len(REMINDER_MESSAGES)]
        print(f"Reminder {i + 1}: {message}")


# Run directly:
if __name__ == "__main__":
    show_reminders(3)