class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.stack[-1][1] if len(self.stack) != 0 else float("inf"), val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
