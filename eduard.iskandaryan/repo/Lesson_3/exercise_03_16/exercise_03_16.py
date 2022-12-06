numbers = input("Please input two numbers: ").split()
num1, num2 = map(int, numbers)
if num1 == num2:
    print("These numbers are equal.")
else:
    print(f"{max(numbers)} is larger")