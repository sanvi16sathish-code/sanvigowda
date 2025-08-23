class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node("eggs")
n2 = Node("ham")
n3 = Node("spam")
n1.next = n2
n2.next = n3

class Singly:
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
                print(current.data)
                current = current.next
            current.next = node

    def display(self):
        print(f"{self.head.data}")

n = Singly()
n.append("abc")
n.display()