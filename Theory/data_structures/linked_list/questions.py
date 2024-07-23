from typing import Any
from typing import Union
from single_linked_list_class import LinkedList


class Node:
    def __init__(self, value: Any):
        self.data = value
        self.next = None


def make_a_sentence(head: Node) -> str:
    result = ''
    times = 0
    # pointer = head  # No head as we can assume head is pointer.
    while head:  # while pointer is not None
        if head.data in ['*', '/']:  # check if a value is in the list/iterable.
            if times == 1:  # this if times=1 will be first as it is higher, and we are using 2 if statements.
                # So as it doesnt go into both.
                if head.next:
                    head.next.data = head.next.data.upper()
            if times == 0:
                result += ' '
                times += 1
        else:
            result += head.data
            times = 0
        head = head.next
    return result


def print_ll_with_head(head: Node) -> str:
    pointer = head
    result = ''
    while pointer is not None:
        result += str(pointer.data) + ' -> '
        pointer = pointer.next
    return result[:-4]


def reverse_linked_list(head: Node) -> Node:
    """In place reversal of ll, ie without creating new ll we reverse the current one"""
    pa = None  # Pointer a, which is used for the ll which we keep reversing.
    # the reverse ll's head will be pa at all times.
    pb = head  # head of current ll, which will keep moving forward till it reaches None
    while pb is not None:
        temp = pb.next
        pb.next = pa
        pa = pb
        pb = temp
    return pa


def sum_of_odd_pos(head: Node) -> Union[int, float]:  # Note: Union means that the return could be either float or int.
    pointer = head
    sum_of_odd = 0
    index = 0  # When pointer is head, index=0.
    while pointer is not None:
        # Odd positions.
        if index % 2 != 0:  # NOTE: 0%2 is 0.
            sum_of_odd += pointer.data
        pointer = pointer.next
        index += 1
    return sum_of_odd


def replace_max(head: Node, replacement: Any):  # Think of ll as array and nodes as objects in array.
    pointer = head
    max_node = pointer  # Assume start node is maximum
    while pointer is not None:
        if pointer.data > max_node.data:
            max_node = pointer
        pointer = pointer.next
    max_node.data = replacement


def max_value_replace(head: Node, replacement: Any):
    # To pass a ll only head of the ll is needed, as it has address to all the following values.
    # TODO: Find the maximum value's index
    index = 0
    max_value = -1
    max_index = 0
    pointer = head  # head node
    if pointer is None:
        raise ValueError("LL is empty")
    while pointer is not None:
        if pointer.data > max_value:
            max_value = pointer.data
            max_index = index
        pointer = pointer.next
        index += 1
    # TODO: Replace the data of the Node at that index
    pointer = head
    for i in range(max_index):
        pointer = pointer.next
    pointer.data = replacement


ll = LinkedList()
ll.insert_tail(1)
ll.insert_tail(4)
ll.insert_tail(8)
ll.insert_tail(3)
ll.insert_tail(100)
print(ll)
replace_max(ll.head, 2)  # input is ll.head, which will give all the ll.
# Thus when value is replaced it reflects here.
print(ll)
print(sum_of_odd_pos(ll.head))
print(ll)
print(print_ll_with_head(reverse_linked_list(ll.head)))
print(ll)

ll_to_sentence = LinkedList()
ll_to_sentence.insert_tail("A")
ll_to_sentence.insert_tail("n")
ll_to_sentence.insert_tail("*")
ll_to_sentence.insert_tail("/")
ll_to_sentence.insert_tail("a")
ll_to_sentence.insert_tail("p")
ll_to_sentence.insert_tail("p")
ll_to_sentence.insert_tail("l")
ll_to_sentence.insert_tail("e")
ll_to_sentence.insert_tail("*")
ll_to_sentence.insert_tail("a")
ll_to_sentence.insert_tail("/")
ll_to_sentence.insert_tail("d")
ll_to_sentence.insert_tail("a")
ll_to_sentence.insert_tail("y")
ll_to_sentence.insert_tail("*")
ll_to_sentence.insert_tail("*")
ll_to_sentence.insert_tail("k")
ll_to_sentence.insert_tail("e")
ll_to_sentence.insert_tail("e")
ll_to_sentence.insert_tail("p")
print(ll_to_sentence)
print(make_a_sentence(ll_to_sentence.head))
# NOTE:
# class LinkedList:
#     def __init__(self, head):
#         self.head = head
#
# def reverse_linked_list(linked_list: LinkedList) -> LinkedList:
#     pa = None
#     pb = linked_list.head  # pb is a reference to the linked list's head

#     # ... (linked list reversal logic)

#     linked_list.head = pa  # This modifies the 'head' attribute of the LinkedList object
#     return linked_list
#
# In this modified example, the reverse_linked_list function takes a LinkedList object as an argument,
# which encapsulates the head of the linked list. Inside the function, you can modify the head attribute of the
# LinkedList object, and the changes will be reflected outside the function.
