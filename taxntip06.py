print("Tax and Tip Calculator")
print("======================")
print("")

meal = float(input("Cost of the meal: "))

tax = meal*0.10
tip = meal*0.18
gt = meal + tax + tip

print("Total Cost  = %3.2f" % (gt))
