class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            # find first decrease
            first_swap_index = -1
            for i in range(n - 1, 0, -1):
                # detect decrease
                if nums[i] > nums[i - 1]:
                    first_swap_index = i - 1
                    break

            # helps counter edge case where there is no number greater than nums[first_swap_index]
            second_swap_index = first_swap_index
                    
            # edge case: array is sorted, next permutation is the whole array reversed 
            if first_swap_index == -1:
                reversed(nums)
                
            # find first element greater than nums[first_swap_index]
            else:
                for i in range(n - 1, first_swap_index, -1):
                    # found a number greater than nums[first_swap_index]
                    if nums[i] > nums[first_swap_index]:
                        second_swap_index = i
                        break

            # swap this valley with the first number that is greater than it 
            nums[first_swap_index], nums[second_swap_index] = nums[second_swap_index], nums[first_swap_index]

            # reverse the number from first_swap_index + 1 until the end 
            left, right = first_swap_index + 1, n - 1
            while left < right:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
            # could have also done nums[first_swap_index + 1:] = reversed(nums[first_swap_index + 1:])