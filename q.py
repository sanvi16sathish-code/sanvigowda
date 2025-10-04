queue = []

def enqueue(item):
    queue.append(item)
    print(f"{item} added to the queue.")

def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        item = queue.pop(0)
        print(f"{item} removed from the queue.")

def display():
    print("Queue:", queue)


enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
display()
