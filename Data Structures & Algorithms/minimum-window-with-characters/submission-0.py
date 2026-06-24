from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        countS = defaultdict(int)
        countT = defaultdict(int)

        reslen = len(s)
        res = ""

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have = 0
        need = len(countT)
        l = 0
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r],0) + 1
            if countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need and l <= r:
                if r - l + 1 <= reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                
                countS[s[l]] -= 1
                if countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res
            


        