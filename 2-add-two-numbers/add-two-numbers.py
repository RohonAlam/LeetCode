# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #Approach1 (converting to int and them sum and again create linkedlist)
        """
        curr1 = l1
        num1 = 0
        curr2 =l2
        num2 = 0
        sum = 0
        count = 0
        while curr1:
            num1 += pow(10,count)* curr1.val 
            curr1 = curr1.next
            count += 1
        count = 0
        while curr2 :
            num2 += pow(10,count) * curr2.val 
            curr2 = curr2.next
            count += 1

        sum = num1 + num2

        head = ListNode()
        current = head

        while True :
            current.val = sum % 10
            sum = sum // 10
            if sum == 0 :
                break
        
            current.next = ListNode()
            current = current.next



        return head
"""
        #Approach2 (directly sum using carry)

        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            # Get current digits
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add digits + carry
            total = val1 + val2 + carry

            # Calculate digit and carry
            digit = total % 10
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move pointers if possible
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next