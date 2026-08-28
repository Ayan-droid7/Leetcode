from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c, count in cnt.items() if count % 2 != 0]
        
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: cnt[c] // 2 for c in cnt}
        m = n // 2

        def construct_full(half_list, mid):
            left = "".join(half_list)
            if n % 2 == 1:
                return left + mid + left[::-1]
            return left + left[::-1]

        def try_match_prefix():
            counts = dict(half_counts)
            prefix = []
            for i in range(m):
                tc = target[i]
                if counts.get(tc, 0) > 0:
                    prefix.append(tc)
                    counts[tc] -= 1
                else:
                    return None
            return construct_full(prefix, mid_char)

        exact_pal = try_match_prefix()
        if exact_pal is not None and exact_pal > target:
            return exact_pal

        for i in range(m - 1, -1, -1):
            counts = dict(half_counts)
            prefix = []
            valid_prefix = True
            for j in range(i):
                tc = target[j]
                if counts.get(tc, 0) > 0:
                    prefix.append(tc)
                    counts[tc] -= 1
                else:
                    valid_prefix = False
                    break
            
            if not valid_prefix:
                continue

            target_c = target[i]
            possible_chars = sorted([c for c, count in counts.items() if count > 0 and c > target_c])
            
            if possible_chars:
                chosen = possible_chars[0]
                prefix.append(chosen)
                counts[chosen] -= 1
                
                for c in sorted(counts.keys()):
                    prefix.extend([c] * counts[c])
                
                res = construct_full(prefix, mid_char)
                return res

        if n % 2 == 1:
            counts = dict(half_counts)
            prefix = []
            valid_prefix = True
            for j in range(m):
                tc = target[j]
                if counts.get(tc, 0) > 0:
                    prefix.append(tc)
                    counts[tc] -= 1
                else:
                    valid_prefix = False
                    break
            
            if valid_prefix and mid_char > target[m]:
                res = construct_full(prefix, mid_char)
                return res

        return ""