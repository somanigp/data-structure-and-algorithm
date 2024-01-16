from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    stack = []
    cur = head
    i = 0
    # length of a linked list
    while head:
        head = head.next
        i += 1
    # Appending the first half in stack
    for _ in range(int(i / 2)):
        stack.append(cur.val)
        cur = cur.next
    if i % 2 != 0:  # If odd number of length, skip the middle Node.
        cur = cur.next
    # checking if the first half is palindrome to second half
    for _ in range(int(i / 2)):
        if not cur:  # it will break if cur is None
            break
        if cur.val != stack.pop():  # Using pop like this will also remove an element from the list.
            return False
        cur = cur.next
    return len(stack) == 0


# Second Approach: reverse the back half of the linked list
# The first challenge then becomes finding the middle of the linked list in order to start our reversing process there.
# For that, we can look to Floyd's Cycle Detection Algorithm.
# With Floyd's, we'll travel through the linked list with two pointers, one of which is moving twice as fast as the
# other.When the fast pointer reaches the end of the list, the slow pointer must then be in the middle.
def is_second_palindrome(head: ListNode) -> bool:
    slow, fast, prev = head, head, None
    while fast and fast.next:  # for odd: slow reaches middle and fast at the end,
        # for even: slow reaches len/2 + 1 and fast reaches None
        slow, fast = slow.next, fast.next.next
    prev, slow, prev.next = slow, slow.next, None  # prev.next none, so that in last while loop, its not a infinite loop
    while slow:
        slow.next, prev, slow = prev, slow, slow.next  # Reverse a Linked List
    fast, slow = head, prev
    while slow:
        if fast.val != slow.val:
            return False
        fast, slow = fast.next, slow.next
    return True


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next = c
c.next = d

print(is_second_palindrome(a))
