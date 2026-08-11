# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast :
            slow = slow.next # skipping the middle if odd length
        
        # reverse the right part

        prev = None
        current = slow
        current_next = slow

        while current :
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next
        
        left = head 
        right = prev

        while left and right :
            if left.val != right.val :
                return False
            left = left.next
            right = right.next
        
        return True


        