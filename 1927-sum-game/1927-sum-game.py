class Solution:
    def sumGame(self, num: str) -> bool:
        h = len(num) // 2
        s1 = sum(int(c) for c in num[:h] if c != '?')
        s2 = sum(int(c) for c in num[h:] if c != '?')
        c1 = num[:h].count('?')
        c2 = num[h:].count('?')
        return (c1 + c2) % 2 != 0 or float(s1 - s2) != (c2 - c1) * 4.5