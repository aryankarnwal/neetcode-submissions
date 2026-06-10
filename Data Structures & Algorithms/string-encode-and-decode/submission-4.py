class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            encoded = str(len(string)) + '.' + string
            res += encoded
            
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            length = ''

            while i < len(s) and s[i] != '.':
                length += s[i]
                i += 1
            length = int(length)
            res.append(s[i+1:i+length+1])
            i += length + 1
        return res
