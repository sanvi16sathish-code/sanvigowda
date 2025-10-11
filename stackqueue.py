class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

class StackQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, item):
        self.stack_in.push(item)

    def dequeue(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        if self.stack_out.is_empty():
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def __str__(self):
        in_items = self.stack_in.items.copy()
        out_items = self.stack_out.items.copy()
        return f"Queue (approx): in: {in_items}, out: {out_items[::-1]}"

if __name__ == "__main__":
    q = StackQueue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q)

    print(q.dequeue())
    print(q)

    q.enqueue(4)
    print(q)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    try:
        q.dequeue()
    except IndexError as e:
        print("Error:", e)
