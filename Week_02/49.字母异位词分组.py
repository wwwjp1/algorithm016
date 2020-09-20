#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (63.42%)
# Likes:    469
# Dislikes: 0
# Total Accepted:    106.5K
# Total Submissions: 167.6K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hashtable = {}
        for item in sorted(strs):
            sortedStr = "".join(sorted(item))
            hashtable[sortedStr] = hashtable.get(sortedStr, []) + [item]
        return [*hashtable.values()]
        '''

        ht = {}
        for item in sorted(strs):
            key = tuple(sorted(item))
            ht[key] = ht.get(key, []) + [item]
        return [*ht.values()]

# @lc code=end
