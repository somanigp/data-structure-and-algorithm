from typing import Union
# From root directory start importing
# from Theory.data_structures.linked_list.single_linked_list_class import LinkedList


class Node:
    def __init__(self, value):
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
        result += pointer.data
        pointer = pointer.next
    # Or you can empty the second stack, pop one by one from pointer and put in other stack
    # and then print it.
    return result[::-1]


print(reverse_string("hello_govind"))
print(text_editor("hello", "uu"))
