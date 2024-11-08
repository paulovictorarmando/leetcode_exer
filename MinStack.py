#min-stack
class MinStack:
    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(0)

    def top(self) -> int:
        if self.stack:
            return self.stack[0]
        return None
    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        return None
"""
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(3)
    print(min_stack.getMin())
"""
