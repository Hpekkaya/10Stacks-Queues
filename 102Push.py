
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
            print(temp.value)
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



my_stack = Stack(1)

start, end, inc = 2, 6, 1

for i in range(start, end, inc):
    my_stack.push(i)

my_stack.print_stack()

