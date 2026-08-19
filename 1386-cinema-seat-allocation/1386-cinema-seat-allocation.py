class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reserved = {}
        for row, seat in reservedSeats:
            reserved[row] = reserved.get(row, 0) | (1 << (seat - 1))
        ans = 2 * (n - len(reserved))
        left = 0b0000011110    # seats 2-5
        middle = 0b0001111000  # seats 4-7
        right = 0b0111100000   # seats 6-9  (fixed)
        for mask in reserved.values():
            l = (mask & left) == 0
            m = (mask & middle) == 0
            r = (mask & right) == 0
            if l and r:
                ans += 2
            elif l or m or r:
                ans += 1
        return ans