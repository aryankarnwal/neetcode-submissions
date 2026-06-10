class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = {}

        for i in nums:
            bucket[i] = bucket.get(i, 0) + 1
        
        for i in range(len(nums)):
            if 0 in bucket and bucket[0] > 0:
                replace = 0
                bucket[0] -= 1
            elif 1 in bucket and bucket[1] > 0:
                replace = 1
                bucket[1] -= 1
            elif 2 in bucket and bucket[2] > 0:
                replace = 2
                bucket[2] -= 1
            nums[i] = replace
        return nums
