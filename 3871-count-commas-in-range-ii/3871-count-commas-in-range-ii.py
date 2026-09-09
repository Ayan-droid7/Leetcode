class Solution:
    def countCommas(self, n: int) -> int:
        return sum(max(0, n - 10**(3 * i) + 1) for i in range(1, 6))