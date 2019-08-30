import math

s = int(input("length of the polygon's side : "))
n = int(input("number of sides : "))

a = (n * s * s)/(4 * math.tan(math.pi / n))

print("The area of the polygon is %3.2f" % a)
