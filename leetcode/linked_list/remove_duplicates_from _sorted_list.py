from typing import Optional


class ListNode:  # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    dummy = ListNode()
    dummy.next = head
    while head.next is not None:
        while head.val == head.next.val:
            head.next = head.next.next
            if head.next is None:
                break
        head = head.next
        # if head is None: # not needed
        #     break
    return dummy.next




