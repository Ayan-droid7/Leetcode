from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr, num_of_letters = [], 0
        
        for word in words:
            if len(curr) + num_of_letters + len(word) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr.append(word)
            num_of_letters += len(word)
            
        res.append(' '.join(curr).ljust(maxWidth))
        return res