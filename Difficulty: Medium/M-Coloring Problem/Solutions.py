class Solution:

    def graphColoring(self, V, edges, m):

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [0] * V

        def isSafe(node, c):

            for neighbour in adj[node]:
                if color[neighbour] == c:
                    return False

            return True

        def backtrack(node):

            if node == V:
                return True

            for c in range(1, m + 1):

                if isSafe(node, c):

                    color[node] = c

                    if backtrack(node + 1):
                        return True

                    color[node] = 0

            return False

        return backtrack(0)
