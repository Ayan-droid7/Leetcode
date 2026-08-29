import bisect

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        start_vals = [s[0] for s in starts]
        
        res = []
        for _, end in intervals:
            idx = bisect.bisect_left(start_vals, end)
            
            if idx < len(start_vals):
                res.append(starts[idx][1])
            else:
                res.append(-1)
                
        return res