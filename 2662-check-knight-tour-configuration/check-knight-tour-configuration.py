class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        # Knight tour must start from top-left
        if grid[0][0] != 0:
            return False

        positions = [None] * (n * n)

        # Store the position of every step
        for row in range(n):
            for col in range(n):
                positions[grid[row][col]] = (row, col)

        # Check every consecutive move
        for i in range(n * n - 1):
            r1, c1 = positions[i]
            r2, c2 = positions[i + 1]

            row_diff = abs(r1 - r2)
            col_diff = abs(c1 - c2)

            if (row_diff, col_diff) not in [(1, 2), (2, 1)]:
                return False

        return True