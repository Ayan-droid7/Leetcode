class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            if c1 == num:
                count1 += 1
            elif c2 == num:
                count2 += 1
            elif count1 == 0:
                c1, count1 = num, 1
            elif count2 == 0:
                c2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        return [c for c in (c1, c2) if c is not None and nums.count(c) > len(nums) // 3]