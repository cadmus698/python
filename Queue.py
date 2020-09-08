queuestr = input('What\'s the queue?(Seperate with commas)\n')
queue = queuestr.split(',')
while True:
    todo = input('What do you want to do\n')
    if todo == 'dequeue' or todo == 'Dequeue':
        print(queue[0])
        queue.remove(queue[0])
    if todo == 'Add' or todo == 'add':
        toadd = input('What should I add?\n')
        queue.append(toadd)
    if todo == 'print' or todo == 'Print':
        print(queue)
    if todo == 'q':
        print('k, byeeeeee')
        break