# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris Inorder traversal 

        res = []

        current = root

        while current :
            # situation 1 : No left node
            if not current.left :
                res.append(current.val)
                current = current.right
            else :
                pred = current.left

                # Threads doesn't exist

                while pred.right and pred.right != current :
                    pred = pred.right
                
                if pred.right == None:
                    pred.right = current
                    current = current.left
                else:
                    pred.right = None
                    res.append(current.val)
                    current = current.right
        
        return res

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

        """
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
        """


