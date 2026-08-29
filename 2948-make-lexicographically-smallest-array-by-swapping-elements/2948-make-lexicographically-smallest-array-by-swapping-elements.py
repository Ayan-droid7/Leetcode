class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        sorted_nums = sorted([(nums[i], i) for i in range(n)])
        res = [0] * n
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_nums[j][0] - sorted_nums[j-1][0] <= limit:
                j += 1
            
            indices = sorted(sorted_nums[k][1] for k in range(i, j))
            
            for idx, k in zip(indices, range(i, j)):
                res[idx] = sorted_nums[k][0]
                
            i = j
            
        return res