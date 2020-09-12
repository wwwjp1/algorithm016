#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (42.97%)
# Likes:    690
# Dislikes: 0
# Total Accepted:    162.9K
# Total Submissions: 379.1K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 暴力
        '''
        for _ in range(k):
            previous = nums[-1]
            for i in range(len(nums)):
                previous, nums[i] = nums[i], previous
        return nums
        '''

        # 2.new array, loop nums i --> (i+k) % len(nums)
        '''
        n = len(nums)
        k = k % n
        temp = [0] * n
        for i in range(n):
            temp[(i+k)%n] = nums[i]
        nums[:] = temp[:]
        return nums
        '''

        # 3. 3 times reverse
        k = k % len(nums)
        def reverse(sta, end, nums):
            while sta < end:
                nums[sta], nums[end] = nums[end], nums[sta]
                sta += 1
                end -= 1
            return nums
        
        nums = reverse(0, len(nums)-1, nums)
        nums = reverse(0, k-1, nums)
        nums = reverse(k, len(nums)-1, nums)
        return nums
# @lc code=end

