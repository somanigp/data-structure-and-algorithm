from typing import Any, Union
# From root directory start importing
# from Theory.data_structures.linked_list.single_linked_list_class import LinkedList


class Node:
    def __init__(self, value: Any):
        self.data = value
        self.next = None


# space complexity : O(n) -> No of inputs = no of nodes. As it is very high with large input,
# generally stack is not used to reverse string. We split the list in 2 and swap values.
def reverse_string(inp: str) -> str:  # Time Complexity: O(2n) -> O(n)
    """Reversing a string using a stack."""
    pointer: Union[Node, None] = None  # Use this as top and keep adding nodes here
    for i in range(len(inp)):  # For all elements in input string.
        new_node = Node(inp[i])  # adding values in ll through head.
        new_node.next = pointer
        pointer = new_node
    result = ''
    while pointer:
        result += pointer.data
        pointer = pointer.next
    return result


def text_editor(str_input: str, instructions: str) -> str:
    # Will require 2 stacks.
    pointer: Union[Node, None] = None
    for i in range(len(str_input)):
        new_node = Node(str_input[i])
        new_node.next = pointer
        pointer = new_node
    storage = []  # This will be treated as a stack through array.
    for i in range(len(instructions)):
        if instructions[i] == 'u':
            storage.append(pointer.data)
            pointer = pointer.next
        else:
            new_node = Node(storage.pop())
            new_node.next = pointer
            pointer = new_node
    result = ''
    while pointer:
        # Easy way to print reverse of a stack.
        # The pop value will be before the already existing values, thus printing from the bottom.***
        result = pointer.data + result
        pointer = pointer.next
    return result


# Comparing 2 and selecting one, comparison and elimination -> stack
def find_celebrity(mat: Any) -> Union[int, None]:
    # With O(n^2) we can brute force this.
    # But with stacks its O(4n) -> O(n).
    pointer: Union[None, Node] = None
    for i in range(len(mat)):
        new_node = Node(i)
        new_node.next = pointer
        pointer = new_node
    while pointer.next:  # Till only one number remains in stack. That will be pointer ie stack with only 1 element.
        a = pointer.data
        b = pointer.next.data
        if mat[a][b] == 1:   # a knows b so a is not celeb.
            pointer = pointer.next
        else:  # else means its 0 and no need for mat[a][b] == 0.
            # As everyone knows the celeb, b is not celeb.
            pointer.next = pointer.next.next  # Skipping b
    # Now there is only one possibility, now need to check if there is no celebrity
    # We are checking if the celebrity knows no one.
    for i in range(len(mat)):
        if i == pointer.data:  # It doesn't matter if the celebrity knows itself.
            continue
        if mat[pointer.data][i] == 1:
            return None
    # Check if everyone knows the celebrity.
    for i in range(len(mat)):
        if i == pointer.data:  # It doesn't matter if the celebrity knows itself.
            continue
        if mat[i][pointer.data] == 0:
            return None
    return pointer.data


def balanced_parenthesis(inp_str: str) -> bool:
    # Check valid parenthesis.
    pointer: Union[Node, None] = None
    parenthesis_tracker = {")": "(",
                           "}": "{",
                           "]": "["}
    for char in inp_str:
        if char in "({[":
            new_node = Node(char)
            new_node.next = pointer
            pointer = new_node
        elif char in ")}]":
            if pointer is None:  # Meaning nothing to remove, meaning no ([{ in stack.
                return False
            if pointer.data != parenthesis_tracker.get(char):  # Meaning proper parenthesis are not matching.
                return False
            else:
                pointer = pointer.next  # If matching pop.
    return pointer is None  # Stack should be empty.


print(reverse_string("hello_govind"))
print(text_editor("hello", "uu"))
mat1 = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]
print(find_celebrity(mat1))
print(balanced_parenthesis("([{a+b}*c] + [a-b]) {}"))
