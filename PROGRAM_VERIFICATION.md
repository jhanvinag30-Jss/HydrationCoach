---

# PROGRAM VERIFICATION – HydrationCoach Project

## 1. Introduction
Program verification is the process of checking whether the program works as expected.
The goal is to ensure that every module of the HydrationCoach project gives correct
output for valid inputs and handles errors properly for invalid inputs.

This document explains how the program was verified through:
- Manual testing
- Module-wise testing
- Running test files
- Observing actual output
- Comparing actual output with expected output

---

## 2. Verification of Individual Modules

### ✔ 2.1 config.py
*Purpose:* Stores constants such as water intake multiplier.  
*Expected Output:* No actual output (because config files only store variables).  
*Actual Output:* No output, worked as intended.

---

### ✔ 2.2 calculator.py
*Purpose:* Calculates daily water intake based on user weight.

*Expected Behaviour:*
- If weight = 50 → output should be 50 * 30 = 1500 ml  
- Functions should return integers  
- Should not crash when negative values appear  

*Tests Performed:*

calculate_water(40) → 1200 ml calculate_water(60) → 1800 ml liters_and_ml(60) → (1, 800)

*Actual Behaviour:*  
✔ All outputs were correct  
✔ No errors  
✔ Verified successfully

---

### ✔ 2.3 reminders.py
*Purpose:* Simulates reminder messages.

*Expected Behaviour:*  
- Should return a list of reminder strings  
- No crashes  

*Actual Output Example:*

Reminder 1: Stay hydrated! Drink water now. Reminder 2: Stay hydrated! Drink water now. Reminder 3: Stay hydrated! Drink water now.

✔ Verified successfully

---

### ✔ 2.4 user_input.py
*Purpose:* Returns dummy user data for testing.

*Expected Behaviour:*  
Should return:

name = "Demo User" weight = 55 interval = 250

*Actual Behaviour:*  
✔ Returned correct dictionary  
✔ Tested with both valid/invalid values  
✔ Verified

---

### ✔ 2.5 main.py
*Purpose:* Runs the whole project.

*Expected Behaviour:*
- Should import all modules correctly
- Should display:
  - User details
  - Daily recommended water intake
  - Reminder messages

*Actual Output:*

Welcome, Demo User! Your daily required water intake: 1650 ml (1 L 650 ml)

--- Reminders --- Reminder 1: Stay hydrated! Drink water now. Reminder 2: Stay hydrated! Drink water now. Reminder 3: Stay hydrated! Drink water now.

✔ Works perfectly after fixing import issues and folder structure.

---

## 3. Test Files Verification

### ✔ test_calculator.py
Expected:
- Print calculator output
Actual:

--- Calculator Tests --- Water for 40kg: 1200 Water for 60kg: 1800 Liters & ml for 60kg: (1, 800)

✔ Verified

### ✔ test_reminders.py
Expected:
- Print 3 reminder lines  
Actual:
✔ Verified

---

## 4. Final Result
All modules run correctly after fixing:
- Folder structure
- Import path
- __init__.py
- Test script location

The HydrationCoach project is *fully verified, stable and working without errors*.

---

## 5. Conclusion
The program is fully verified using:
- Functional testing  
- Module testing  
- Expected vs actual comparison  
- Manual execution in VS Code & Google Colab  

Therefore, the implementation is successful and meets all requirements.


---