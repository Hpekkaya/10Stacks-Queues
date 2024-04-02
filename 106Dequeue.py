class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(f"{temp.value}", end=" ")
            temp = temp.next
        print(f"\nLength of Queue : {self.length}")

    def enqueue(self, value):
        new_node = Node(value)
        # check length if 0 new
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        # else add
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node
        # inc length
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None

        self.length -= 1
        return temp


my_queue = Queue(1)

start, end, inc = 2, 6, 1
for i in range(start, end, inc):
    my_queue.enqueue(i)

print("Before Dequeue :")
my_queue.print_queue()


print(f"\nAfter Dequeue : {my_queue.dequeue().value}")
my_queue.print_queue()
