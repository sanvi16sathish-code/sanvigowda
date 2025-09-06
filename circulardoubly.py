class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoubly:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
        else:
            tail = self.head.prev
            tail.next = node
            node.prev = tail
            node.next = self.head
            self.head.prev = node
        self.size += 1

    def display_forward(self):
        if not self.head:
            print("List is empty.")
            return
        print("Forward:")
        current = self.head
        while True:
            print(current.data, end=" <-> " if current.next != self.head else "\n")
            current = current.next
            if current == self.head:
                break

    def display_backward(self):
        if not self.head:
            print("List is empty.")
            return
        print("Backward:")
        current = self.head.prev 
        while True:
            print(current.data, end=" <-> " if current.prev != self.head.prev else "\n")
            current = current.prev
            if current == self.head.prev:
                break

cdll = CircularDoubly()
cdll.append("eggs")
cdll.append("ham")
cdll.append("spam")

cdll.display_forward()
cdll.display_backward()
