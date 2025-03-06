from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        rotten, fresh = set(), set()
        time = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))

        while fresh:
            if not rotten: return -1

            temp = set()

            for i, j in rotten:
                for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (i + direction[0], j + direction[1]) in fresh:
                        temp.add((i + direction[0], j + direction[1]))

            rotten = temp
            fresh -= rotten
            time += 1

        return time

