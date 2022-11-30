small_cup = 0.10
large_cup = 0.25
large_count = int(input("Please enter number of returned large cups: "))
small_count = int(input("Please enter number of returned small cups: "))
print(f"You will be refunded ${float((small_cup * small_count)) + (large_cup * large_count)} from all cups.")