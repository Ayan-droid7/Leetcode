import math
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        lcms = []
        for i in range(1, len(coins) + 1):
            for combo in combinations(coins, i):
                lcms.append((math.lcm(*combo), 1 if i % 2 == 1 else -1))
        
        left, right = 1, min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if sum(sign * (mid // l) for l, sign in lcms) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans