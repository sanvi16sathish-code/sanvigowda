class Stack:
    def __init__(self, max_size=None):
        self.stack = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        if self.max_size is None:
            return False
        return len(self.stack) >= self.max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Cannot push:", item)
            return
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from empty stack.")
            return None
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.stack):
                print(item)



if __name__ == "__main__":
    s = Stack(max_size=5)

    s.push(10)
    s.push(20)
    s.push(30)
    s.display()

    print("Top element is:", s.peek())

    s.pop()
    s.display()

    s.pop()
    s.pop()
    s.pop() 
    s.push(40)
    s.push(50)
    s.push(60)
    s.push(70)
    s.push(80)
    s.push(90)  
    s.display()
