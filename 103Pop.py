class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(f"{temp.value}", end=" ")
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            # self.top.next = new_node
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp



my_stack = Stack(1)

start, end, inc = 2, 6, 1

for i in range(start, end, inc):
    my_stack.push(i)

print(f"Before the Pop")
my_stack.print_stack()

my_stack.pop()
print(f"\nAfter the Pop")
my_stack.print_stack()


