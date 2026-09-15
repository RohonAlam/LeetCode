# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.seq = 0
        self.result = None

        def inorder(node):
            if not node and self.result is not None :
                return

            if node.left :
                inorder(node.left)
            
            self.seq += 1

            if self.seq == k :
                self.result = node.val
                return

            if node.right :
                inorder(node.right)

        
        inorder(root)
        return self.result
    
        # Approach 2
        """
        self.seq = 0

        def inorder(node):
            if not node:
                return None

            # 1. Left
            result = inorder(node.left)

            if result is not None:
                return result

            # 2. Visit current node
            self.seq += 1

            if self.seq == k:
                return node.val

            # 3. Right
            return inorder(node.right)

        return inorder(root)
        """
            
        