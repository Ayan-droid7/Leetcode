class Solution:
    def minSumOfLengths(self, arr: [int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        min_len = float('inf')
        ans = float('inf')
        
        prefix_sum = 0
        sum_map = {0: -1}
        
        for i in range(n):
            prefix_sum += arr[i]
            sum_map[prefix_sum] = i
            
        prefix_sum = 0
        current_min = float('inf')
        
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum - target in sum_map:
                left = sum_map[prefix_sum - target]
                length = i - left
                if left >= 0 and dp[left] != float('inf'):
                    ans = min(ans, length + dp[left])
                current_min = min(current_min, length)
            dp[i] = current_min
            
        return ans if ans != float('inf') else -1