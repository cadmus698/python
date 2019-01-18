from time import sleep
a = int(input("Enter the first number\n"))
sleep(1)
b = int(input("Enter the second number\n"))
sleep(1)
d = 0 
af = []
bf = []
if a > b:
    while ((d + 1) >= 1) and:
        d = d + 1
        if (a % d == 0):
            af.append(d)
        else:
            pass
abf = [val for val in af if val in bf]
if len(abf) == 0:
    print("1")
else:
    print(max(abf))

        
