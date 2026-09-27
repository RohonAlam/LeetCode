"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        
        visited = {}
        
        def dfs(node):
            # nonlocal visited
            if node in visited :
                return visited[node]

            # creating new node
            root = Node(node.val)
            
            visited[node] = root

            for neighbor in node.neighbors :                               
                root.neighbors.append(dfs(neighbor))
                                         
            return root
        
        return dfs(node)



        

        