"""
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        visited = set()
        total_cost = 0

        def mindistance():

            distance = float('inf')
            next_point = None

            # Check every point already in the MST
            for x, y in visited:

                # Find the closest unvisited point
                for point in points:

                    a, b = point

                    if (a, b) not in visited:

                        current_distance = abs(x - a) + abs(y - b)

                        if current_distance < distance:
                            distance = current_distance
                            next_point = point

            # Add the selected point to the MST
            visited.add((next_point[0], next_point[1]))

            return distance

        # Start from any point
        visited.add((points[0][0], points[0][1]))

        # We need n - 1 edges to connect n points
        for _ in range(len(points) - 1):

            total_cost += mindistance()

        return total_cost
"""


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        n = len(points)

        # Minimum cost to connect each point
        # to the current MST
        min_dist = [float('inf')] * n

        # Whether the point is already in MST
        visited = [False] * n

        # Start from point 0
        min_dist[0] = 0

        ans = 0

        for _ in range(n):

            # Find the unvisited point with
            # minimum connection cost
            u = -1

            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            # Add this point to MST
            visited[u] = True
            ans += min_dist[u]

            # Update distances of remaining points
            for v in range(n):

                if not visited[v]:

                    x1, y1 = points[u]
                    x2, y2 = points[v]

                    cost = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[v] = min(min_dist[v], cost)

        return ans

                
        