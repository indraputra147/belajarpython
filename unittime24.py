h = int(input("hours : "))
m = int(input("minutes "))
s = int(input("seconds : "))

t1 = h*3600
t2 = m*60

total = t1 + t2 + s

print("Total second is ", total)
