#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (61.33%)
# Likes:    249
# Dislikes: 0
# Total Accepted:    137.8K
# Total Submissions: 224.4K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 示例 1:
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 说明:
# 你可以假设字符串只包含小写字母。
# 
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted and compere
        
        # hashmap
        '''
        slist, tlist = [0] * 26, [0] * 26
        for i in s:
            slist[ord(i) - ord("a")] += 1
        for j in t:
            tlist[ord(j) - ord("a")] += 1
        return slist == tlist
        '''

        # map count
        hashset = {}
        for i in s: hashset[i] = hashset.get(i, 0) + 1
        for j in t: hashset[j] = hashset.get(j, 0) - 1
        for h in hashset: 
            if hashset[h] == 0: return True
        return False 
# @lc code=end
