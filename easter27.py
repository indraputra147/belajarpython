import math

y = int(input("Input a year : "))

a = y % 19
b = math.floor(y / 100)
c = y % 100
d = math.floor(b / 4)
e = b % 4
f = math.floor((b + 8) / 25)
g = math.floor((b - f + 1) / 3)
h = (19*a + b - d - g + 15) % 30
i = math.floor(c / 4)
k = c % 4
l = (32 + 2*e + 2*i - h - k) % 7
m = math.floor((a + 11*h + 22*l) / 451)
month = math.floor((h + 1 - 7*m + 114) / 31)
day = 1 +((h + l - 7*m + 114) % 31)

print("The date of Easter in this year is at ", day)
print("month ", month)
