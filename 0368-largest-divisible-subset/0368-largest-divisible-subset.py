class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        nums.sort()
        dp = [1] * len(nums)
        parent = [-1] * len(nums)
        max_len, max_idx = 1, 0
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len, max_idx = dp[i], i
                
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = parent[max_idx]
            
        return res[::-1]