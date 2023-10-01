#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        done = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(i, len(nums)):
                    if nums[j] <= nums[i-1]:
                        j = j-1
                        break
                
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = nums[i:][::-1]
                done = True
                break

        if not done:
            nums.sort() 
        
# @lc code=end

