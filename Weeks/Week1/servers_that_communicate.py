class Solution:
    def countServers(self, grid: list) -> int:
        total = 0
        rows = [0 for i in range(len(grid))]
        cols = [0 for j in range(len(grid[0]))]

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    rows[i] += 1
                    cols[j] += 1
                    total += 1

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1 and rows[i] == 1 and cols[j] == 1:
                    total -= 1

        return total
