# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        if not root:
            return True

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # Both null -> symmetric branch
            if not t1 and not t2:
                return True
        # One null, or values don't match -> asymmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False

        # Mirror check: left vs right AND right vs left
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)
        """
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            t1, t2 = queue.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # Add opposing branches to queue
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True