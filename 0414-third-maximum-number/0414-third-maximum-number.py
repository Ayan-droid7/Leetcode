class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = None
        
        for num in nums:
            # Skip duplicates of already tracked maximums
            if num in (first, second, third):
                continue
            
            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num
                
        # If third maximum doesn't exist, return the overall maximum (first)
        return third if third is not None else first