class Stack:
    def __init__(self):
        self.z1 = []

    def basic(self):
        self.z1.append(10)
        self.z1.append(2)
        self.z1.append(7)
        self.z1.append(12)
        print(self.z1)

    def basic2(self):
        self.z1.insert(16, 7) 
        print(self.z1)
my_stack = Stack()
my_stack.basic()   
my_stack.basic2()  
