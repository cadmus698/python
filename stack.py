stackinput = input("What's the stack(seperate with commas)\n")
stack = stackinput.split(',')
print(stack[-1])
def stackCount():
    global stack
    print(len(stack))
def pop():
    global stack
    print(stack[-1])
    number = -1
    thingtoadd = ''
    newstack = []
    while thingtoadd != stack[-2]:
        number += 1
        thingtoadd = stack[number]
        newstack.append(thingtoadd)
    stack = newstack
def push(n):
    global stack
    stack.append(n)
def display():
    global stack
    print(stack)
while True:
    function = input('What should I do?\n1. Count,\n2. Pop,\n3. Push\n4. Display\n')
    if function == '1':
        stackCount()
    
    elif function == '2':
        pop()
            
    elif function == '3':
        newnum = (input('What should I push?\n'))
        push(newnum)
        
    elif function == '4':
        display()
        
    elif function == 'q':
        break