n = input("Enter the numerator.\n")
d = input("Enter the denominator.\n")
n1 = input("Enter the 2nd numerator.\n")
d1 = input("Enter the 2nd denominator.\n")


n = int(n) * int(d1)
d2 = int(d) * int(d1)

n1 = int(n1) * int(d)
d1 = int(d1) * int(d)

n = int(n) + int(n1)

n = str(n)
d = str(d2)

print(n + "/" + d)