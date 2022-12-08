class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#       All integers is distinct, use this condition.
#       Sort and swap neighbours into small, big, small, big pattern
#       Time O(sort), Space O(sort)
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i], nums[i - 1] = nums[i -1], nums[i]
        return nums