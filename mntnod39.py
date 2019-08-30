m = input("Input name of a month (lowercase) : ")

if m == "january" or m == "march" or m == "auly" or m == "august" or m == "october" or m == "december":
    result = "31 days"
elif m == "february":
    result = "28 or 29 days"
elif m == "april" or m == "may" or m == "june" or m == "september" or m == "november":
    result = "30 days"

print("There are " + result + " in", m)
