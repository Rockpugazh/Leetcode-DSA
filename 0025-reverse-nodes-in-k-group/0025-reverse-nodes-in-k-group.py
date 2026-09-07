class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while True:
            # Find kth node
            kth = prev

            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            # Reverse k nodes
            curr = prev.next
            next_group = kth.next
            previous = next_group

            while curr != next_group:
                temp = curr.next
                curr.next = previous
                previous = curr
                curr = temp

            # Connect reversed group
            temp = prev.next
            prev.next = kth
            prev = temp