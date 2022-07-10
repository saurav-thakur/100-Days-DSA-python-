
# https: // leetcode.com/problems/min-stack/
# https: // www.youtube.com/watch?v = ZvaRHYYI0-4 & list = PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd & index = 12

class MinStack:

    def __init__(self):
        self.stack = []
        self.minEle = None

    def push(self, val: int) -> None:

        if len(self.stack) == 0:
            self.minEle = val
            self.stack.append(val)

        elif val < self.minEle:

            self.stack.append(2*val-self.minEle)
            self.minEle = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None

        elif self.stack[-1] < self.minEle:
            self.minEle = 2*self.minEle - self.stack[-1]
            self.stack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        elif self.stack[-1] < self.minEle:
            return self.minEle

        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.minEle
