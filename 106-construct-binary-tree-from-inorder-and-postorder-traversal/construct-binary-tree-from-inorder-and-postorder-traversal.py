# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        index_map = {
            value : index for index,value in enumerate(inorder)
        }

        postorder_index = len(postorder)-1

        def build(left,right):
            nonlocal postorder_index
            if left>right :
                return None
            
            root_value = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_value)

            mid = index_map[root_value]
            root.right = build(mid+1,right)

            root.left = build(left,mid-1)

            

            return root
        return build(0,len(inorder)-1)

        