from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        grid = classroom

        start = None
        litter_positions = []
        for i in range(m):
            row = grid[i]
            for j in range(n):
                c = row[j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litter_positions.append((i, j))

        L = len(litter_positions)
        if L == 0:
            return 0

        full_mask = (1 << L) - 1
        size_mask = 1 << L

        litter_idx = [[-1] * n for _ in range(m)]
        for idx, (i, j) in enumerate(litter_positions):
            litter_idx[i][j] = idx

        blocked = [[False] * n for _ in range(m)]
        is_reset = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 'X':
                    blocked[i][j] = True
                elif c == 'R':
                    is_reset[i][j] = True

        sr, sc = start

        def idx3(r, c, mask):
            return (r * n + c) * size_mask + mask

        best = [-1] * (m * n * size_mask)
        start_ind = idx3(sr, sc, 0)
        best[start_ind] = energy

        q = deque()
        q.append((sr, sc, energy, 0, 0))

        while q:
            r, c, e, mask, dist = q.popleft()
            if mask == full_mask:
                return dist
            if e == 0:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if blocked[nr][nc]:
                    continue
                ne = e - 1
                nmask = mask
                if is_reset[nr][nc]:
                    ne = energy
                else:
                    li = litter_idx[nr][nc]
                    if li >= 0 and not (mask >> li) & 1:
                        nmask = mask | (1 << li)
                ind = idx3(nr, nc, nmask)
                if ne > best[ind]:
                    best[ind] = ne
                    q.append((nr, nc, ne, nmask, dist + 1))

        return -1