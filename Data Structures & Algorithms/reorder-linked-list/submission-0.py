# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        fast, slow = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        head2 = head
        tail2 = prev

        while tail2.next:
            HN = head2.next
            TN = tail2.next
            head2.next = tail2
            tail2.next = HN
            head2 = HN
            tail2 = TN
        