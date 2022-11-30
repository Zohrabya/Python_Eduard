meal_cost = float(input("Please enter the cost of the meal: "))
meal_tax = meal_cost * 10/100
meal_tip = meal_cost * 18/100

print(f"Your tax amount is {round(meal_tax, 2)}, tip amount is {round(meal_tip, 2)} and the grand total is {round(meal_cost + meal_tax + meal_tip, 2)}")