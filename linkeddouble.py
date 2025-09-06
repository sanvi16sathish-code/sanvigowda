class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
        self.size += 1

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    def display_backward(self):
        current = self.head
        if current is None:
            return

     
        while current.next:
            current = current.next

    
        while current:
            print(current.data, end=" <-> " if current.prev else "\n")
            current = current.prev


d = Doubly()
d.append("eggs")
d.append("ham")
d.append("spam")

print("Forward:")
d.display_forward()

print("Backward:")
d.display_backward()
