from typing import Optional
# list1: Optional[ListNode]: This indicates that the parameter list1 is expected to be of type Optional[ListNode].
# The Optional type hint from the typing module signifies that the parameter can either be of the specified
# type (ListNode in this case) or None.
#
# list2: Optional[ListNode]: Similar to list1, this indicates that the parameter list2 is expected to be of type
# Optional[ListNode], meaning it can either be a list of ListNode elements or None.
#
# -> Optional[ListNode]: This part of the signature specifies the return type of the method. In this case,
# it indicates that the method can return either a ListNode or None.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:  # not list1 -> checks if the list is empty
        return list1
    if not list1 or not list2:
        return list1 if not list2 else list2
    current_node1 = list1
    current_node2 = list2
    cur = dummy = ListNode()
    while current_node1 is not None and current_node2 is not None:
        if current_node1.val < current_node2.val:
            cur.next = current_node1
            cur = cur.next
            current_node1 = current_node1.next
        elif current_node1.val > current_node2.val:
            cur.next = current_node2
            cur = cur.next
            current_node2 = current_node2.next
        else:
            cur.next = current_node1
            cur = cur.next
            current_node1 = current_node1.next
            cur.next = current_node2
            cur = cur.next
            current_node2 = current_node2.next
    if current_node1 is None:
        if current_node2 is None:
            return dummy.next
        else:
            while current_node2 is not None:
                cur.next = current_node2
                cur = cur.next
                current_node2 = current_node2.next
            return dummy.next
    if current_node2 is None:
        while current_node1 is not None:
            cur.next = current_node1
            cur = cur.next
            current_node1 = current_node1.next
        return dummy.next


l1 = ListNode(10)
l12 = ListNode(20)
l13 = ListNode(50)
l1.next = l12
l12.next = l13

l2 = ListNode(10)
l22 = ListNode(30)
l23 = ListNode(40)
l24 = ListNode(60)
l2.next = l22
l22.next = l23
l23.next = l24

list_final = merge_two_lists(l1, l2)

while list_final is not None:
    print(list_final.val)
    list_final = list_final.next


# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     cur = dummy = ListNode()
#     while list1 and list2:
#         if list1.val < list2.val:
#             cur.next = list1
#             list1, cur = list1.next, list1
#         else:
#             cur.next = list2
#             list2, cur = list2.next, list2
#
#     if list1 or list2:
#         # if list1 checks if list1 is None
#         cur.next = list1 if list1 else list2  # Adding 2 Linked lists **** points 1st tail to 2nd head.
#
#     return dummy.next

