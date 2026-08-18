# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
        

        