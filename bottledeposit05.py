print("deposit for : ")
print("- small container (< 1 Liter) is $0.10 ")
print("- big container (> 1 Liter) is $0.25 ")
print(" ")
m = int(input("Input the number of small size container : "))
x = int(input("Input the number of big size container : "))


tm = m*0.10
tx = x*0.25
tr = tm+tx

print("Total Refunds : %3.2f" % (tr))
