class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f"Popped {popped}")
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        print("Stack (top to bottom):")
        while current:
            print(current.data)
            current = current.next

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    print("Top element is:", stack.peek())
    stack.pop()
    stack.display()
