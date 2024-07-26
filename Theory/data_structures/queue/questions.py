# Making a queue if 2 stacks are given: Queue behaviour using 2 stacks - Enqueue and Dequeue
# s1 - Use to only enqueue. Add only in s1
# When dequeue : If s2 empty and s1 empty: no element in queue
#              : if s2 empty, s1 not, pop all the items in s1 and put one by one in s2. Then pop through s2 - dequeue
#              : if s2 not empty then directly pop from s2

from Theory.data_structures.stack.main import Stack


class Queue:
    def __init__(self):
        self.s1: Stack = Stack()  # Stack object
        self.s2: Stack = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if not self.s2.is_empty():
            self.s2.pop()
        if self.s2.is_empty() and not self.s1.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
            self.s2.pop()
        if self.s1.is_empty() and self.s2.is_empty():
            raise ValueError("Queue is empty")

    def __str__(self):
        return str(self.s1) + '\n' + str(self.s2)


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que)
que.dequeue()
print(que)
