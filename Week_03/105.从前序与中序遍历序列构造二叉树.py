#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (68.17%)
# Likes:    693
# Dislikes: 0
# Total Accepted:    117.9K
# Total Submissions: 172.9K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTreeHelper(pre_left: int, pre_right: int, in_left:int, in_right:int):
            if pre_left > pre_right: return None

            root_pre = pre_left
            root_val = preorder[root_pre]
            root_in = hashmap[root_val]

            left_tree_size = root_in - in_left

            root = TreeNode(root_val)
            root.left = buildTreeHelper(pre_left+1, pre_left+left_tree_size, in_left, root_in-1)
            root.right = buildTreeHelper(pre_left+left_tree_size+1, pre_right, root_in+1, in_right)

            return root

        hashmap = {elem: i for i, elem in enumerate(inorder)}
        n = len(preorder)-1
        return buildTreeHelper(0, n, 0, n)

# @lc code=end

