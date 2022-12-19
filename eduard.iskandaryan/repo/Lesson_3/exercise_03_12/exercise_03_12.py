less_one_liter = 0.10
more_one_liter = 0.25
large_cups = int(input("Please enter number of returned large cups: "))
small_cups = int(input("Please enter number of returned small cups: "))
refund = "{:.2f}".format((less_one_liter * small_cups) + (more_one_liter * large_cups))
print(f"You will be refunded ${refund} from all cups.")