import collections


class Solution:
    def solve(self, board: list) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        untouchables = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in untouchables and board[i][j] == "O":
                    start, valid = (i, j), True
                    visited = {start}
                    queue = collections.deque([start])

                    while queue:
                        current = queue.popleft()
                        for d in directions:
                            new = new_i, new_j = current[0] + d[0], current[1] + d[1]
                            if not (0 <= new_i < len(board) and 0 <= new_j < len(board[0])):
                                valid = False
                            elif new not in visited and board[new_i][new_j] == "O":
                                visited.add(new)
                                queue.append(new)

                    for row, col in visited:
                        if valid:
                            board[row][col] = "X"
                        else:
                            untouchables.add((i, j))
