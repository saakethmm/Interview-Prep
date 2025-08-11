from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

        self.q2 = self.q1.copy()
        while self.q1:
            self.q1.popleft()

    def pop(self) -> int:
        t = self.q2[0]
        self.q2.popleft()
        return t

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return not self.q2