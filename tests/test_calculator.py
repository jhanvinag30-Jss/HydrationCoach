"""
Manual tests for the calculator module.
"""

from hydration_coach.calculator import recommended_ml, recommended_liters


def run():
    print("Running calculator tests...\n")

    assert recommended_ml(40) >= 1500
    print("✔ Minimum requirement check passed")

    assert recommended_ml(60) == 60 * 35
    print("✔ Formula correctness test passed")

    assert recommended_liters(70) == round((70 * 35) / 1000, 2)
    print("✔ Liter conversion test passed")

    print("\nAll calculator tests passed!")


if _name_ == "_main_":
    run()
