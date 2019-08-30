#input length and width in feet. output in acres

l = float(input("Lenght of the field : "))
w = float(input("Width of the field : "))

a = w*l

a = a/43560

print("The area of the field is", a, "acres" )
