# Handles input operations and basic validation using loops and conditionals.
def get_weight_from_user():
  while True:
    user_input=input("Enter your weight in kg:")
    if user_input.isdigit():
      return int(user_input)
    else:
      print("Please enter a valid number.")

def get_today_intake():
  while True:
    user_input=input("How much water have you drink today (ml)?")
    if user_input,isdigits():
       return int(user_input)
else: 
   print("Enter a valid number.")
