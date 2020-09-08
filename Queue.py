queuestr = input('What\'s the queue?(Seperate with commas)\n')
queue = queuestr.split(',')
queue1 = []
while True:
    todo = input('What do you want to do\n')
    if todo == 'dequeue' or todo == 'Dequeue':
        print(queue[0])
        num = 1
        toend = False
        while True:
            if toend == True:
                break
            if queue[num] == queue[-1]:
                toend = True
            queue1.append(queue[num])
            num += 1
        queue = queue1
        pass
    if todo == 'Add' or todo == 'add':
        toadd = input('What should I add?\n')
        queue.append(toadd)
    if todo == 'print' or todo == 'Print':
        print(queue)
    if todo == 'q':
        print('k, byeeeeee')
        break