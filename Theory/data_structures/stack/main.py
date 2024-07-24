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


# stack = Stack()
# print(stack.is_empty())
# stack.push(2)  # Will be last
# stack.push(1)
# stack.push(0)  # Last in as of now.
# print(stack)
# stack.pop()
# print(stack)
# print(len(stack))
# print(stack.peek())


# Stack through array:
stack_arr = [1, 2, 3]
stack_arr.append(4)  # Adding from top
stack_arr.pop()  # Removing from top


# class Stack through list:
class ArrStack:
    def __init__(self, size: int):  # Since we are making stack out of array like from java, c++,
        # thus array is fixed size.
        """We are assuming it is java/c++ stack thus of fixed size."""
        self.size = size
        self.stack = [None] * self.size  # print([None] * 2)  # [None, None]
        self.top = -1  # 1st element to be put at index 0, so when no. of elements = 1, index = 0.
        # Thus top starts with -1

    def push(self, value: Any):
        # When stack with size 3 is created. top can take these values: 0, 1, 2 ( starts with -1)
        # Thus size is length and last index is len-1. Thus when last possible index (2) + 1 == size (3). Stack is full.
        if self.top + 1 == self.size:  # or self.top == self.size - 1, which means last index=len-1
            raise ValueError("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self) -> Any:
        if self.top == -1:
            raise ValueError("Stack is empty")
        value = self.stack[self.top]  # self.top is index of topmost value in the stack.
        self.stack[self.top] = None
        self.top -= 1  # Reducing the index, so it represents the now topmost element.
        return value

    def __len__(self):
        """No. of non-empty elements in the stack."""
        return self.top + 1  # index of topmost element + 1 == len. Thus when lenght is 0 self.top = -1. (-1 + 1 = 0)

    def __str__(self) -> str:
        res = ''
        for i in range(self.top, -1, -1):  # From topmost index to 0
            res += str(self.stack[i]) + '->'
        return res[:-2]


arr_stack = ArrStack(size=5)
arr_stack.push(5)
arr_stack.push(4)
arr_stack.push(3)
arr_stack.pop()
print(len(arr_stack))
print(arr_stack)

