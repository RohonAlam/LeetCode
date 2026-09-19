# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:

        if not preorder:
            return None

        inorder = sorted(preorder)
        
        val_idx =  { val : index for index,val in enumerate(inorder)}
        preorder_index = 0

        def rebuild(left,right):
            nonlocal preorder_index
            if left > right :
                return None
            val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(val)

            mid = val_idx[val]

            root.left = rebuild(left,mid-1)
            root.right = rebuild(mid+1,right)

            return root
        
        return rebuild(0,len(preorder)-1)

        # print(val_idx)
        