class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = dict()
        for i in range(len(nums)):
            needComp = target - nums[i]
            if needComp in myHash:
                return [myHash[needComp], i]
            else: 
                myHash[nums[i]] = i
        