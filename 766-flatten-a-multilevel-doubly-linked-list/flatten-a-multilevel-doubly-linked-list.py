"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head 

        while temp :
            if temp.child :
                pt1 = temp.next
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None
                pt2 = temp.next
                while pt2.next:
                    pt2 = pt2.next
                pt2.next = pt1
                if pt1:
                    pt1.prev = pt2
            temp = temp.next
        return head

        