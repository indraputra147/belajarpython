import math

r = int(input("Input a radius of a circle in meter: "))

a = math.pi * r * r
v = 4 * math.pi * r * r * r / 3

print("The Area of the circle is %3.2f" % a)
print("The Volume of the circle is %3.2f" % v)
