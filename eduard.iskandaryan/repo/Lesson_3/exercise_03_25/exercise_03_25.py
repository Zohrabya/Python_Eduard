number = int(input("Please enter four digit number: "))
num1 = number // 1000
num2 = (number - num1 * 1000) // 100
num3 = (number - num1 * 1000 - num2 * 100) // 10
num4 = (number - num1 * 1000 - num2 * 100 - num3 * 10)
print(f"{num1} + {num2} + {num3} + {num4} = {num1 + num2 + num3 + num4}")