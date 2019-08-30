print("MPG to L/100 km converter")
print("=========================")
print("")

x = float(input("Insert fuel efficiency in MPG : "))

# 1 miles = 1.60934 km
# 1 gallon = 3.78541 Liter

y = (100*3.78541)/(x*1.60934)

print("The fuel efficiency is %3.2f" % (y))



