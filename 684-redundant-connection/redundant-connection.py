class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        parent = {}

        def find(i) :
            if i not in parent :
                parent[i] = i

            if parent[i] != i :
                parent[i] = find(parent[i])
            """
            if parent.setdefault(i,i) != i :
                parent[i] = find(parent[i])
            """
            return parent[i]

        def union(i,j) :
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j :
                return False

            parent[root_i] = root_j
            return True

        for a,b in edges :
            if not union(a,b) :
                return [a,b]
        
        return []
                