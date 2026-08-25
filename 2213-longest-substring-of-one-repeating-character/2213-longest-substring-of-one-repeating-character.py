class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        S = list(s)
        
        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        
        def build(node, l, r):
            if l == r:
                tree_max[node] = tree_pref[node] = tree_suff[node] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, l, mid, r)
            
        def merge(node, l, mid, r):
            left = 2 * node
            right = 2 * node + 1
            
            tree_max[node] = tree_max[left] if tree_max[left] > tree_max[right] else tree_max[right]
            tree_pref[node] = tree_pref[left]
            tree_suff[node] = tree_suff[right]
            
            if S[mid] == S[mid + 1]:
                combined = tree_suff[left] + tree_pref[right]
                if combined > tree_max[node]:
                    tree_max[node] = combined
                if tree_pref[left] == mid - l + 1:
                    tree_pref[node] += tree_pref[right]
                if tree_suff[right] == r - mid:
                    tree_suff[node] += tree_suff[left]
                    
        def update(node, l, r, idx):
            if l == r:
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx)
            else:
                update(2 * node + 1, mid + 1, r, idx)
            merge(node, l, mid, r)
            
        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            S[idx] = char
            update(1, 0, n - 1, idx)
            ans.append(tree_max[1])
            
        return ans