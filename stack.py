from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, val):
        self.q2.append(val)
        print self.q2

        while len(self.q1) > 0:
            self.q2.append(self.q1[0])
            self.q1.pop()
        q = self.q1
        self.q1 = self.q2
        self.q2 = q

        print("q1", self.q1)
        print("q2", self.q2)


    def pop(self):
        return self.q1.popleft()


if __name__ == '__main__': 
    s = Stack() 
    s.push(1)
    s.push(2)
    print(s.pop())
