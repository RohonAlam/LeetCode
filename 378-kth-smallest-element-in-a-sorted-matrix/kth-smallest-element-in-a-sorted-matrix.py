import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        min_heap = [(matrix[0][0],0,0)]

        visited = {(0,0)}

        for _ in range(k-1):
            val , r , c = heapq.heappop(min_heap)

            if c+1 < n and (r,c+1) not in visited :
                heapq.heappush(min_heap, (matrix[r][c+1],r,c+1))
                visited.add((r,c+1))
            if r+1<n and (r+1,c) not in visited :
                heapq.heappush(min_heap,(matrix[r+1][c],r+1,c))
                visited.add((r+1,c))
        
        return min_heap[0][0]
            