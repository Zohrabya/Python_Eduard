numbers = input("Please enter 2 integers: ").split()
num1, num2 = map(int, numbers)
if num1 % num2 == 0:
    print("First number is a multiple of the second.")
else:
    print("First number is not a multiple of the second.")