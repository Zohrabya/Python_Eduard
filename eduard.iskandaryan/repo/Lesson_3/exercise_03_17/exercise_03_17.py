all_numbers = input("Input three different integers: ").split()
num1, num2, num3 = map(int, all_numbers)
sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3
print(f"Sum is {sum}")
print(f"Average is {average}")
print(f"Product is {product}")
print(f"Smallest is {min(all_numbers)}")
print(f"Largest is {max(all_numbers)}")