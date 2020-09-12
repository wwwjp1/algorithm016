#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1.hashset
        hashset = {}
        for i in range(len(nums)):
            if hashset.get(target - nums[i]) is not None: return [hashset[target - nums[i]], i]
            hashset[nums[i]] = i
        

        # 2. 双指针+sort+new array
        '''
        n = len(nums)
        temp = nums.copy()
        temp.sort()
        l = 0
        r = n - 1
        while l < r:
            if temp[l] + temp[r] == target:
                break
            elif temp[l] + temp[r] < target:
                l += 1
            else:
                r -= 1
        fir = nums.index(temp[l])
        nums.pop(fir)
        sec = nums.index(temp[r])
        if sec >= fir: sec += 1
        return [fir, sec]
        '''
# @lc code=end