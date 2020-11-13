#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Method: 记录数组中所有的0，然后补上
        nums_len = len(nums)
        nums_zero = 0
        i = 0
        while i < nums_len:
            if nums[i] == 0:
                nums_zero += 1
                nums.pop(i)
                nums_len -= 1
            else:
                i += 1
        for _ in range(nums_zero):
            nums.append(0)
# @lc code=end

