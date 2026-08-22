class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p, t = 0, 1, n
        while t:
            s += t % 10
            p *= t % 10
            t //= 10
        return n % (s + p) == 0