class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path, current_sum):
            if len(path) == k:
                if current_sum == n:
                    res.append(path[:])
                return
            
            for i in range(start, 10):
                if current_sum + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, current_sum + i)
                path.pop()
                
        backtrack(1, [], 0)
        return res