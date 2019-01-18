from time import sleep
a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
c = a * b
d = 0
e = 1
vars = []
if a % b == 0:
    print(a)
elif b % a == 0:
    print(b)
else:
    while ((d + 1) < a and (d + 1) < b):
        d = d + 1
        e = c % d
        if e == 0:
            vars.append(c/d)
    low = min(vars)
    if low%a == 0:
        if low > 1:
            print(int(low))
        elif  low <= 1:
            print("1")
        else:
            print("Sorry...")
            sleep(1)
            print("I couldn't crack that one.")
        
    else:
        print("Sorry...")
        sleep(1)
        print("I couldn't crack that one")


    

