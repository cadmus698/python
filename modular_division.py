while True:
    num1 = input("Enter the first number.\n")
    num2 = input("Enter the second number.\n")
    if int(num1) > int(num2):
        (a) = float(int(num1)/int(num2))
        b = str(a).index('.')
        c = (str(a)[:(b)])
        d = int(num2) * int(c)
        e = int(num1) - int(d)
        print("The answer is " + str(c) + " with a remainder of " + str(e))
        break
    elif int(num2) > int(num1):
        (a) = float(int(num2)/int(num1))
        b = str(a).index('.')
        c = (str(a)[:(b)])
        d = int(num1) * int(c)
        e = int(num2) - int(d)
        print("The answer is " + str(c) + " with a remainder of " + str(e))
        break
    elif int(num1) == int(num2):
        print("1")
        break
    else:
        print('Whup! That\'s weird! Something went wrong! Pls try again.')
