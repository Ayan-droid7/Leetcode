class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        arr = sorted(nums)
        mid = (len(nums) + 1) // 2
        nums[::2] = arr[:mid][::-1]
        nums[1::2] = arr[mid:][::-1]