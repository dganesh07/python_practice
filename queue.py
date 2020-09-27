class Queue: 
    def __init__(self): 
        self.s1 = [] 
        self.s2 = [] 

    def enQueue(self, val):
        # push oly to stack 1
        self.s1.append(val)

    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Queue empty")
        elif len(self.s2) == 0 and len(self.s1) > 0:
            # transfer s1 items to s2 oly if s2 is empty
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            val = self.s2.pop()
            return val


if __name__ == '__main__': 
    q = Queue() 
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
  
    print(q.deQueue()) 
    print(q.deQueue()) 
    print(q.deQueue())
       


