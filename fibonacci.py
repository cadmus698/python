from time import sleep

print("Hi! Welcome to the Fibonacci's generator!")
sleep(1)
x = input("How many elements of the Fibonacci sequence would you like me to calculate?\n")

a = 0
one = 1
two = 1
three = (one + two)
print("Calculating...")
sleep(1)
a = a + 1
if int(x) >= (a):
    print(one)
a = a + 1
sleep(0.5)
if int(x) >= (a):
    print(two)
a = a + 1
sleep(0.5)
if int(x) >= (a):
    print(three)
sleep(0.5)
while True:
    a = a + 1
    if int(x) >= (a):
        one = (two + three)
        print(one)
    a = a + 1
    sleep(0.5)
    if int(x) >= (a):
        two = (three + one)
        print(two)
    a = a + 1
    sleep(0.5)
    if int(x) >= (a):
        three = (one + two)
        print(three)
    else:
        break