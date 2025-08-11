from collections import deque


class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()   

    def push(self, x: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2