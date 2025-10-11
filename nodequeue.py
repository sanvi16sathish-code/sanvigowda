class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        result = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return result

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return "Queue: " + str(elements)

if __name__ == "__main__":
    q = LinkedListQueue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q)               # Output: Queue: [10, 20, 30]
    print(q.dequeue())     # Output: 10
    print(q.peek())        # Output: 20
    print(q)               # Output: Queue: [20, 30]