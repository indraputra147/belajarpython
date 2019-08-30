import math

#t1, t2 = float(input("Input coordinate 1 : ")).split()
t1 = float(input("input latitude 1 : "))
g1 = float(input("input longitude 1 : "))
t2 = float(input("input latitude 2 : "))
g2 = float(input("input longitude 2 : "))

d = 6371.01 * math.acos(math.sin(math.radians(t1))*math.sin(math.radians(t2)) + math.cos(math.radians(t1))*math.cos(math.radians(t2))*math.cos(math.radians(g1 - g2)))

print("Distance between point 1 and point 2 is", d)
