class Solution:
    def maximalRectangle(self, matrix: list) -> int:
        if not matrix:
            return 0
        right, down = (0, 1), (1, 0)
        width = {}

        def traverse_right(current):
            nonlocal matrix, width, right
            if current in width:
                return width[current]

            new = (current[0] + right[0], current[1] + right[1])
            if new[1] >= len(matrix[0]) or matrix[new[0]][new[1]] == "0":
                width[current] = 1
            else:
                width[current] = 1 + traverse_right(new)

            return width[current]

        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == "1" and num not in width:
                    traverse_right((i, j))

        result = 0

        def traverse_down(current, min_width, height=0):
            nonlocal matrix, result, width, down

            new_width = min(min_width, width[current])
            area = new_width * (height + 1)

            result = max(result, area)

            new = (current[0] + down[0], current[1] + down[1])
            if new[0] < len(matrix) and matrix[new[0]][new[1]] == "1":
                traverse_down(new, new_width, height + 1)

        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == "1":
                    current = (i, j)
                    traverse_down(current, width[current])
        return result
