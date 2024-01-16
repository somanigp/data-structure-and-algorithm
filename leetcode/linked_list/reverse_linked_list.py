from typing import Optional


class ListNode:  # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    cur = dummy = ListNode()
    original_head = head  # Save the head of linked list somewhere
    while original_head.next is not None:
        while head.next.next is not None:
            head = head.next
        cur.next = head.next
        cur = cur.next
        head.next = None
        head = original_head  # To restart from the start of linked list again
    cur.next = original_head
    return dummy.next

# Change the direction of pointer:
# Need 3 variables: prev (starts with none as current head needs to point to none) , current and next
# Step 1: Save next so later cur can become next (nxt = current.next)
# Step 2: Current should point to prev (current.next = prev)
# step 3: prev should be current node (increment)
# step 4: current should be next node which we saved earlier (increment)


def reverse_list_better(head: Optional[ListNode]) -> Optional[ListNode]:  # Time complexity: O(n)
    # and Space complexity: O(1)
    current = head
    prv = None
    while current:  # while current means while current exists and is not null
        nxt = current.next
        current.next = prv
        prv = current
        current = nxt
    return prv


def reverse(self, head):  # Through Recursion

    # If head is empty or has reached the list end
    if head is None or head.next is None:
        return head

    # Reverse the rest list
    rest = self.reverse(head.next)

    # Put first element at the end
    # Reversing a pointer **NOTE**
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest
