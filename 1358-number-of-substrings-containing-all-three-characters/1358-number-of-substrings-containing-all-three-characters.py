class Solution:

  def numberOfSubstrings(self, s: str) -> int:
    ans = 0
    count = {c: 0 for c in 'abc'}

    l = 0
    for c in s:
      count[c] += 1
      while min(count.values()) > 0:
        count[s[l]] -= 1
        l += 1

      ans += l

    return ans