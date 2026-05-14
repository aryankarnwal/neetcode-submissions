class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last = ''
        prefix = ''
        min_len = float('inf')
        for string in strs:
            if len(string) < min_len:
                min_len = len(string)
        if len(strs) == 1:
            return strs[0]
        for i in range(min_len):
            
            for j in range(len(strs)):
                
                if j == 0:
                    last = strs[j][i]
                    continue
                else:
                    if j == len(strs)-1 and strs[j][i]==last:
                        prefix += strs[j][i]
                        last = strs[j][i]
                    elif strs[j][i] == last:
                        last = strs[j][i]
                        continue
                    else:
                        return prefix
        return prefix
                

                



        