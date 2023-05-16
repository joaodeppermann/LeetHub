class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # curSum = 0
        # maxSum = -inf
        # for i in range(len(nums)):
        #     curSum += nums[i]
        #     maxSum = max(maxSum, curSum)
        #     if curSum < 0:
        #         curSum = 0
        # return maxSum

        # Divide and Conquer
        
        # get the maximum subarray that passes through the middle 
        # divide the array into two parts
        # recurse 
        
        # base case
        if len(nums) == 1:
            return nums[0]
        
        mid = (len(nums) - 1) // 2 # last element of the left half
        
        # get the best sum of the left subarray 
        best_left = -inf
        mysum = 0
        for i in range(mid, -1 , -1):
            mysum += nums[i]
            best_left = max(best_left, mysum)
            
        # get the best sum of the right subarray 
        best_right = -inf
        mysum = 0
        for i in range(mid + 1, len(nums)):
            mysum += nums[i]
            best_right = max(best_right, mysum)
        
        ans = max(best_right + best_left, self.maxSubArray(nums[:mid + 1]), self.maxSubArray(nums[mid + 1:]))
        return ans
        
        # SC = log(N)
        # TC = Nlog(N)