
class Stack:

    def __init__(self,size):
        self.size = size
        self.top = 0
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def isFull(self):
        if self.top == self.size:
            return True
        return False

    def push(self,element):
        
        if self.isFull():
            print("Stack Overflow!!. Cannot push more Items")
            return
        self.stack.append(element)
        self.top += 1

    def pop(self):

        if self.isEmpty():
            print("Stack Underflow!!. Cannot pop more Items")
            return

        idx = self.top
        self.top -=1
        ans = self.stack[idx-1]

        del self.stack[ans]


    def peek(self):
        print(self.stack[self.top-1])

    def print_all_elements(self):

        if self.isEmpty():
            print("Satck is Empty!!")

        for i in self.stack:
            print(i,end=",")


stack = Stack(5)
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
# stack.push(4)
# stack.push(8)
stack.peek()

stack.pop()
stack.push(4)
stack.push(8)

stack.print_all_elements()

    
        


