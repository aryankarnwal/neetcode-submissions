class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + '.'
            encoded += s
        return encoded
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '.':
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            res.append(s[i: i + length])
            i += length
        return res

