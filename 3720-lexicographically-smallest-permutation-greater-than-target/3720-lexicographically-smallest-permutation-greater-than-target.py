from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        s_counts = Counter(s)
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            req_counts = Counter(target[:i])
            if all(s_counts[c] >= req_counts[c] for c in req_counts):
                rem_counts = s_counts - req_counts
                available_chars = []
                for c, count in rem_counts.items():
                    available_chars.extend([c] * count)
                valid_chars = [c for c in available_chars if c > target[i]]
                if valid_chars:
                    best_char = min(valid_chars)
                    available_chars.remove(best_char)
                    available_chars.sort()
                    return target[:i] + best_char + "".join(available_chars)
                    
        return ""