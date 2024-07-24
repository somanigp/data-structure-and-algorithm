# Stacks: DS based on LIFO (Last In, First Out). Eg: plates in mess.
# Can be made out of both array and ll.

# Has top: open-ended and bottom: close-ended.
# Operations from top: push(append), pop, peek (shows the topmost item), is_empty (if stack is empty),
# size (no. of items in stack)

# Stack through ll : your top will be head and all operations, insert and delete will be performed through head/top.
from typing import Any, Union


class Node:
    def __init__(self, value: Any):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        # Condition of empty stack
        self.top: Union[Node, None] = None
        # self.n = 0

    def is_empty(self) -> bool:
        """Returns if stack is empty or not."""
        return self.top is None  # Expression will be either True or False and will return that.

    def push(self, value) -> None:
        """Add value to stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> None:
        """Remove topmost value of the stack"""
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            self.top = self.top.next

    def __str__(self) -> str:
        pointer = self.top
        result = ''
        while pointer:
            result += str(pointer.data) + '->'
            pointer = pointer.next
        return result[:-2]

    def peek(self) -> Any:
        if not self.is_empty():
            return self.top.data
        raise ValueError("Stack is empty")

    def __len__(self) -> int:
        index = 0
        pointer = self.top
        while pointer:
            # index should be incremented before going to next pointer
            # as it will add +1 for first node then move, and so on
            index += 1
            pointer = pointer.next
        return index


stack = Stack()
print(stack.is_empty())
stack.push(2)  # Will be last
stack.push(1)
stack.push(0)  # Last in as of now.
print(stack)
stack.pop()
print(stack)
print(len(stack))
print(stack.peek())
