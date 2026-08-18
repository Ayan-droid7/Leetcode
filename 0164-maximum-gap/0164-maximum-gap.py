class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
            
        min_val = min(nums)
        max_val = max(nums)
        
        if min_val == max_val:
            return 0
            
        N = len(nums)
        # Bucket size: minimum possible maximum gap
        B = max(1, (max_val - min_val) // (N - 1))
        num_buckets = (max_val - min_val) // B + 1
        
        # Initialize buckets
        buckets_min = [float('inf')] * num_buckets
        buckets_max = [float('-inf')] * num_buckets
        
        # Populate buckets with min and max values
        for num in nums:
            idx = (num - min_val) // B
            if num < buckets_min[idx]:
                buckets_min[idx] = num
            if num > buckets_max[idx]:
                buckets_max[idx] = num
                
        # Calculate the maximum gap
        max_gap = 0
        prev_max = min_val
        for i in range(num_buckets):
            if buckets_min[i] == float('inf'):
                continue  # Skip empty buckets
                
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]
            
        return max_gap