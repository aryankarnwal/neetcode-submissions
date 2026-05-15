class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i,v in enumerate(nums):
            if v != val:
                nums[count] = v
                count += 1
        return count
