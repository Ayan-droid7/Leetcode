from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [item[0] for item in Counter(nums).most_common(k)]