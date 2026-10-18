class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        n = len(grid)
        m = len(grid[0])

        visited = {(0, 0)}
        i, j = 0, 0
        last = (0, 0)

        while True:
            direction = grid[i][j]

            if direction == 'L':
                ni, nj = i, j - 1
            elif direction == 'R':
                ni, nj = i, j + 1
            elif direction == 'U':
                ni, nj = i - 1, j
            else:  # 'D'
                ni, nj = i + 1, j

            if not (0 <= ni < n and 0 <= nj < m):
                return list(last)

            if (ni, nj) in visited:
                return list(last)

            i, j = ni, nj
            visited.add((i, j))
            last = (i, j)