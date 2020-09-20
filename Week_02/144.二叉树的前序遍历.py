#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 1. recursion
        '''
        ans = []
        def helper(curr):
            if curr:
                ans.append(curr.val)
                if curr.left: helper(curr.left)
                if curr.right: helper(curr.right)
        helper(root)
        return ans
        '''

        # 2.stack 
        stack = []
        ans = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return ans
# @lc code=end
