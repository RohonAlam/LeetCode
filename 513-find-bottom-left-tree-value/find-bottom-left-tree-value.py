# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root :
            return []

        queue = deque([root])



        while queue :
            level_size = len(queue)
            current_level = []
            leftmost = queue[0].val
            

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            
            leftmost = current_level[0]
            
        
        return leftmost
            
                






        