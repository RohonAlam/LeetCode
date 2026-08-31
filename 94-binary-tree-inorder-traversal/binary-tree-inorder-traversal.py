# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #implementation 1 : using a function
        """
        res = []

        def traverse(node) :
            if not node:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return res 
        """
        #Implementation 2 : using while loop

        res , stack = [] , []
        curr = root

        while curr or stack :

            while curr :
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)

            curr = curr.right
        
        return res

