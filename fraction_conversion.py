whole_number = input("Enter the whole number.\n")
numerator = input("Enter the numerator.\n")
denominator = input("Enter the denominator.\n")
if int(whole_number) > 0:
    a = int(whole_number) * int(denominator)
    b = int(a) + int(numerator)
    print(str(b) + "/" + str(denominator))
elif int(whole_number) == 0:
    n = int(numerator)/int(denominator)
    o = str(n).index(".")
    v = (str(n)[:o])
    x = int(numerator) % int(denominator)
    if v == "0":
        print(str(x) + "/" + str(denominator))
    else:
        print(str(v) + " " + str(x) + "/" + str(denominator))
        