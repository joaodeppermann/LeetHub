class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        # a wiggle sequence is made of ups and downs 
        # ups = when the difference nums[i] - nums[i - 1] > 0
        # downs = when the differnece nums[i] - nums[i - 1] < 0
        # initialize both counts as one because a single element counts as a wiggle sequence 
        # up represents the longest wiggle subsequence until the current index that finishes at a up wiggle 
        # down represents the longest wiggle subsequence until the current index that finishes at a down wiggle 
        down, up = 1, 1
        # traverse the array comparing if differences are ups or downs 
        for i in range(1, len(nums)):
            # up detected
            if nums[i] > nums[i - 1]:
                # up gets the value of the current longest subsequence ending at a down wiggle and adds 1 to it 
                up = down + 1
            # down detected
            elif nums[i] < nums[i - 1]:
                # down gets the valut of the current longest subsequence ending at a up wiggle and adds 1 to it
                down = up + 1
        return max(down, up);
    
# SC = O(1)
# TC = O(n)