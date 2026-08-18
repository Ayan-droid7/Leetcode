class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        counts = {}
        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                counts[x] = counts.get(x, 0) + 1
        return max([x for x, c in counts.items() if c == 1], default=-1)