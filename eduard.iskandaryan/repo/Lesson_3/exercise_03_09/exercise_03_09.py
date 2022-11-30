price = int(input("Please enter the price of the meal: "))
tip_percent = int(input("Please enter the tip percent you want to leave: "))
tip_amount = price * tip_percent / 100
print(f"The tip amount is {tip_amount} and total bill is {price + tip_amount}")