class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        best = ""
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    count += 1
                if count == k:
                    sub = s[i:j+1]
                    if not best:
                        best = sub
                    elif len(sub) < len(best):
                        best = sub
                    elif len(sub) == len(best) and sub < best:
                        best = sub
                elif count > k:
                    break
        return best