#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashset

        # double index 夹逼loop and sorted list
        temp = nums.copy()
        temp.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            res = temp[l] + temp[r]
            if  res < target:
                l += 1
            elif res > target:
                r -= 1
            else:
                break
        fir = nums.index(temp[l])
        nums.pop(fir)
        sec = nums.index(temp[r])
        if fir <= sec:
            sec += 1
        return [fir, sec]

        
# @lc code=end
