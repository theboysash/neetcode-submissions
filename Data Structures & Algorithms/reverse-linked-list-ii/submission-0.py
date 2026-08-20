class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        # Step 1: walk to the node just before `left`
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: reverse the sublist from `left` to `right`
        curr = prev.next        # this will end up as the tail of the reversed section
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next