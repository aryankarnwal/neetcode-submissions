class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)

        count = 0
        last = nums[0]

        for i in nums:
            if i == last:
                count += 1
                if count > len(nums)/2:
                    return i
            else:
                count = 1
                last = i
        return nums[0]

        