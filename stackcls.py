class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.items):
                print(item)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()

    print("Top element is:", stack.peek())
    print("Popped element:", stack.pop())
    stack.display()
