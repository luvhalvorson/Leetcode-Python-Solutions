class MinStack:

    def __init__(self):
        self.list = []
        self.min = None


    def push(self, val: int) -> None:
        lastmin = self.getMin()
        if lastmin is None:
            curmin = val
        else:
            curmin = min(lastmin, val)
        self.list.append((val, curmin) )

    def pop(self) -> None:
        self.list.pop()
        
    def top(self) -> int:
        return self.list[-1][0]

    def getMin(self) -> int:
        if not self.list:
            return None
        else:
            return self.list[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()