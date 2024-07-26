# Queue: Linear DS, FIFO (First In, First Out)
# In ll implementation: Insertion: from TAIL, Deletion: from HEAD.
# Add from end of the ll/rear and exit from the start/front
# Insertion: Enqueue, and Deletion: Dequeue.

# Queue using ll
from typing import Any, Union


class Node:
    def __init__(self, value: Any):
        self.data = value
        self.next: Union[None, Node] = None


class Queue:
    def __init__(self):
        self.front: Union[None, Node] = None  # head of the ll
        self.rear: Union[None, Node] = None  # tail of the ll, note we are not just going to use the head this time as with only head,
        # it takes O(n) amt of time to add an element at the end of ll.

    def enqueue(self, value: Any):
        """Add element at rear"""
        new_node = Node(value)
        if self.rear is None:  # When the queue is empty, both front and rear are None. So either condition will do.
            self.front = new_node
            self.rear = self.front  # Rear and front will point to the same node.
        else:  # When there is one or more than one element present. NOTE: front will not move
            self.rear.next = new_node  # adding new node at the end
            self.rear = self.rear.next  # NOTE: here self.rear = new_node also works, as all nodes are independent and
            # only the previous node knows current nodes pos. As in prev step we added that pos in prev node, this also
            # works.

    def dequeue(self) -> Any:
        """Remove element from front"""
        if self.front is None:  # When Queue is empty
            raise ValueError("Empty Queue")
        if self.front == self.rear:  # only 1 element left. ***
            self.rear = None
        new_value = self.front.data
        self.front = self.front.next
        return new_value

    def is_empty(self):
        return self.front is None

    def __len__(self) -> int:
        pointer: Union[None, Node] = self.front
        counter = 0
        while pointer is not None:
            counter += 1
            pointer = pointer.next
        return counter

    def __str__(self) -> str:
        pointer: Union[None, Node] = self.front
        res = ''
        while pointer is not None:
            res += str(pointer.data) + ' '
            pointer = pointer.next
        return res


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que, len(que))
que.dequeue()
que.dequeue()
que.dequeue()
print(que, que.rear)
