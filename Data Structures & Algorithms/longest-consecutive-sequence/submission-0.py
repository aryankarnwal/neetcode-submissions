class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        running = 1

        for i in nums:
            if i - 1 in seen:
                continue

            while (i + 1) in seen:
                running += 1
                i += 1

            res = max(res, running)
            running = 1

        return res        