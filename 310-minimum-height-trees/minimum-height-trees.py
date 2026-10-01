"""
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        Edgelist = {}

        for a, b in edges:
            Edgelist.setdefault(a, []).append(b)
            Edgelist.setdefault(b, []).append(a)

        min_height = float('inf')
        result = []

        for root in range(n):

            queue = deque([(root, 0)])
            visited = [False] * n
            visited[root] = True

            height = 0

            while queue:
                curr, level = queue.popleft()

                height = max(height, level)

                for neighbor in Edgelist.get(curr, []):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, level + 1))

            if height < min_height:
                min_height = height
                result = [root]

            elif height == min_height:
                result.append(root)

        return result
"""
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        # Special case
        if n <= 2:
            return list(range(n))

        # Build adjacency list
        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            degree[a] += 1
            degree[b] += 1

        # Add all initial leaves
        queue = deque()

        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        remaining = n

        # Remove leaves layer by layer
        while remaining > 2:

            # Number of leaves in the current layer
            leaves = len(queue)

            remaining -= leaves

            for _ in range(leaves):

                leaf = queue.popleft()

                # Remove this leaf from the tree
                for neighbor in graph[leaf]:

                    degree[neighbor] -= 1

                    # Neighbor has now become a leaf
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)