# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Approach 1
        """
        if not head or not head.next:
            return head

        # Find length and tail
        size = 1
        tail = head

        while tail.next:
            tail = tail.next
            size += 1

        k %= size

        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail
        steps = size - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break circle
        new_tail.next = None

        return new_head

        """
        #Approach 2

        # Empty list or single node
        if not head or not head.next:
            return head

        # Save original head
        original_head = head

        # Find size and last node
        size = 1
        current = head

        while current.next:
            size += 1
            current = current.next

        last = current

        # Remove unnecessary full rotations
        k %= size

        if k == 0:
            return head

        # Find the new tail
        current = head
        t = 1

        while t != size - k:
            current = current.next
            t += 1

        # current = new tail
        temp = current

        # Node after new tail = new head
        head = current.next

        # Old tail should point to OLD head
        last.next = original_head

        # Break after new tail
        temp.next = None

        return head