# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    cur = head
    final = dummy = ListNode()  # Keep putting the smallest here.
    length_of_ll = 0
    while cur:
        cur = cur.next
        length_of_ll += 1
    prev = None
    cur = head
    ahead = cur.next
    original_head= ListNode()
    i = 0
    for _ in range(length_of_ll):
        while ahead:
            if cur.val < ahead.val:
                if prev is None:
                    cur.next, ahead.next = ahead.next, cur
                    original_head = ahead
                else:
                    prev.next, cur.next, ahead.next = ahead, ahead.next, cur
                prev, ahead = ahead, cur.next
            else:
                if prev is None:
                    prev, cur, ahead = cur, ahead, ahead.next
                    original_head = prev
                else:
                    cur, prev, ahead = cur.next, prev.next, ahead.next
        final.next = cur
        i += 1
        if i == length_of_ll:
            break
        final = final.next
        prev.next = None
        prev = None
        cur = original_head
        ahead = cur.next
    return dummy.next


a = ListNode(3)
b = ListNode(1)
c = ListNode(2)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

x = sort_list(a)
while x:
    print(x.val)
    x = x.next
