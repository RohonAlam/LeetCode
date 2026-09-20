# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.addStack(root)
    
    def addStack(self,node):
        if not node:
            return

        while node :
            self.stack.append(node)
            node = node.left

               

    def next(self) -> int:
        res = self.stack.pop()
        if res.right :
            self.addStack(res.right)
        return res.val

        

    def hasNext(self) -> bool:
        if not self.stack :
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()