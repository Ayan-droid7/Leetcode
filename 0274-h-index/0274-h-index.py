class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)
        
        for c in citations:
            counts[min(c, n)] += 1
            
        h = 0
        for i in range(n, -1, -1):
            h += counts[i]
            if h >= i:
                return i
                
        return 0