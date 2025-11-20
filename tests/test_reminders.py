"""
Manual tests for reminders module.
"""

from hydration_coach.reminders import generate_reminders


def run():
    print("Running reminder tests...\n")

    r = generate_reminders(2000, 250)
    assert len(r) > 0
    print("✔ Reminder creation test passed")

    assert sum(a for _, a in r) >= 2000
    print("✔ Total water goal coverage passed")

    for h, _ in r:
        assert 0 <= h <= 23
    print("✔ Valid hour test passed")

    print("\nAll reminder tests passed!")


if _name_ == "_main_":
    run()
