from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) #key = list with counts per character, value: strings

        for string in strs:
            count = [0]*26
            for c in string:
                count[ord(c)-ord('a')] += 1
            hashmap[tuple(count)].append(string)
        
        ans = []

        for key in hashmap.keys():
            temp = []
            for string in hashmap[key]:
                temp.append(string)
            ans.append(temp)
        
        return ans



