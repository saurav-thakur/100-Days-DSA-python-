class MinStack:

    def __init__(self):
        self.stack = []
        self.supportingStack = []

    def push(self, val: int) -> None:

        if len(self.stack) == 0 or val <= self.supportingStack[-1]:
            self.stack.append(val)
            self.supportingStack.append(val)

        else:
            self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        elif self.supportingStack[-1] == self.stack[-1]:
            self.stack.pop()
            self.supportingStack.pop()

        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.supportingStack) == 0:
            return None
        return self.supportingStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
