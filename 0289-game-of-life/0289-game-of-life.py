class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        def count_live_neighbors(r, c):
            count = 0
            for i in range(max(0, r - 1), min(m, r + 2)):
                for j in range(max(0, c - 1), min(n, c + 2)):
                    if (i != r or j != c) and board[i][j] in (1, 2):
                        count += 1
            return count

        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1