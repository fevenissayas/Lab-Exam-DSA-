
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
 
    def enqueue(self, x):
        self.in_stack.append(x)
 
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    
    def dequeue(self):
        self.peek()
        return self.out_stack.pop()
 
    def empty(self):
        return not self.in_stack and not self.out_stack
    
check = MyQueue ()

check.enqueue (1)
check.enqueue (2)
check.enqueue (3)
print (check.peek())