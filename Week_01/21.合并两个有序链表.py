#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (64.29%)
# Likes:    1260
# Dislikes: 0
# Total Accepted:    365.8K
# Total Submissions: 568.8K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1.recursion
        '''
        def helper(l1, l2):
            if not l1: return l2
            if not l2: return l1
            if l1.val < l2.val:
                l1.next = helper(l1.next, l2)
                return l1
            else:
                l2.next = helper(l1, l2.next)
                return l2
        return helper(l1, l2)
        '''

        # 2.迭代
        preHead = ListNode(-1)
        previous = preHead
        while l1 and l2:
            if l1.val < l2.val:
                previous.next = l1
                l1 = l1.next
            else:
                previous.next = l2
                l2 = l2.next
            previous = previous.next
        previous.next = l1 if l1 is not None else l2
        return preHead.next
# @lc code=end

