# base case, it is possible to go to the end of the array if we are already at the end of the array
# use a goal variable to keep what is the minimum index that we need to reach so we can go until the end

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0