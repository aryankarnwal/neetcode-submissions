class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            length = len(i)
            encoded = encoded + str(length) + '.'
            encoded += i
        print(encoded)
        return encoded
        

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            length = ""
            while s[index] != '.':
                length += s[index]
                index += 1
            length = int(length)
            res.append(s[index+1:index+1+length])
            print(res)
            index += (length+1)
        return res
    
#["neet","code","love","you"]
#4.neet4.code4.love3.you