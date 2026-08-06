class Solution:

    def graphColoring(self, V, edges, m):

        # Convert edge list into adjacency list
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 0 means vertex is currently uncolored
        color = [0] * V

        def isSafe(node, c):

            # Check all neighbours of current node
            for neighbour in adj[node]:

                # Adjacent vertex already has this color
                if color[neighbour] == c:
                    return False

            return True

        def backtrack(node):

            # All V vertices have been colored
            if node == V:
                return True

            # Try every available color
            for c in range(1, m + 1):

                if isSafe(node, c):

                    # Choose
                    color[node] = c

                    # Explore
                    if backtrack(node + 1):
                        return True

                    # Undo
                    color[node] = 0

            # None of the m colors worked
            return False

        return backtrack(0)