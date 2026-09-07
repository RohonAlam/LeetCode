# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(node1, node2):
            # Both trees are empty
            if not node1 and not node2:
                return True

            # Only one tree is empty
            if not node1 or not node2:
                return False

            # Values are different
            if node1.val != node2.val:
                return False

            # Both current nodes match,
            # so compare their children
            return (
                sameTree(node1.left, node2.left)
                and
                sameTree(node1.right, node2.right)
            )

        # Empty subRoot is considered a subtree
        if not subRoot:
            return True

        # root is empty but subRoot isn't
        if not root:
            return False

        # Try matching subRoot starting at current root
        if sameTree(root, subRoot):
            return True

        # Search in left or right subtree
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )
            
