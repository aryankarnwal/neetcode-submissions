class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][0]:
                ptemp, pindex = stack.pop()
                res[pindex] = index - pindex
                
            stack.append((temp, index))
        return res