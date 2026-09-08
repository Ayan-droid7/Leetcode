class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        base = 1000
        while n >= base:
            res += n - base + 1
            base *= 1000
        return res