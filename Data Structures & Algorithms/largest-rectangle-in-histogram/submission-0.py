class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0


        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                latest = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                res = max(res, heights[latest]*width)
            stack.append(i)
        return res
