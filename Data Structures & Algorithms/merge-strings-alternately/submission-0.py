class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''

        least = min(len(word1), len(word2))

        for i in range(least):
            ans += word1[i]
            ans += word2[i]
        
        if least < len(word1):
            ans+= word1[least:]
        if least < len(word2):
            ans+=word2[least:]
        return ans