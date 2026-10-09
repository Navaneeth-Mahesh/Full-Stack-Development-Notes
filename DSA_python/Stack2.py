class Stack2:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if len(self.item) == 0:
            return -1
        return self.item.pop()

    def top(self):
        if len(self.item) == 0:
            return -1
        return self.item[-1]

    def size(self):
        return len(self.item)

stack = Stack2()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.item)
print(stack.pop())
print(stack.top())
print(stack.size())
print(stack.item)