class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            if s[r] not in seen:
                longest = max(r-l+1, longest)
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1  
                seen.add(s[r])
        return longest