from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        rotten = deque()
        fresh, minutes = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while rotten and fresh > 0:

            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1:
                        continue

                    grid[row][col] = 2
                    rotten.append([row, col])
                    fresh -= 1

            minutes += 1


        return minutes if fresh == 0 else -1
