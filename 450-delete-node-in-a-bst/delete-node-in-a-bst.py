# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def predecessor(node):
            current = node

            while current.right:
                current = current.right

            return current

        def successor(node):
            current = node

            while current.left:
                current = current.left

            return current

        def traverse(node, key):
            if not node:
                return None

            # Search left
            if key < node.val:
                node.left = traverse(node.left, key)

            # Search right
            elif key > node.val:
                node.right = traverse(node.right, key)

            # Found the node
            else:

                # --------------------------------
                # Case 1: Leaf node
                # --------------------------------
                if not node.left and not node.right:
                    return None

                # --------------------------------
                # Case 2: No left child
                # Use successor
                # --------------------------------
                # if not node.left:
                #     succ = successor(node.right)

                #     node.val = succ.val

                #     node.right = traverse(node.right, succ.val)

                #     return node
                if not node.left:
                    return node.right

                # --------------------------------
                # Case 3: No right child
                # Use predecessor
                # --------------------------------
                # if not node.right:
                #     pred = predecessor(node.left)

                #     node.val = pred.val

                #     node.left = traverse(node.left, pred.val)

                #     return node
                if not node.right:
                    return node.left

                # --------------------------------
                # Case 4: Both children exist
                # Use predecessor
                # --------------------------------
                pred = predecessor(node.left)

                node.val = pred.val

                node.left = traverse(node.left, pred.val)

            return node

        return traverse(root, key)