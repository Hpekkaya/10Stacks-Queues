class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(stack):
    # assing temp Stack
    temp_stack = Stack()
    # create outer loop (stack)
    while not stack.is_empty():
        temp = stack.pop()
        # create inner loop (temp stack and temp.stak[-1] > temp)
        while (not temp_stack.is_empty()) and (temp_stack.peek() > temp):
            # push to stack(temp_stack.pop)
            stack.push(temp_stack.pop())
        # push to temp_stact (temp)
        temp_stack.push(temp)
    # create a loop transfer from temp to stact
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()





