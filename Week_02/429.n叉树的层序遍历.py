#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (66.46%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    29.7K
# Total Submissions: 44.6K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其层序遍历:
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# 说明:
# 
# 
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # bfs
        '''
        queue = collections.deque([root])
        res = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.extend(curr.children)
            if level: res.append(level)
        return res    
        '''
        
        # dfs
        def helper(root, level):
            if not root: return []
            if len(res) == level:
                res.append([])
            # 结点加入对应level的list中
            res[level].append(root.val)
            for child in root.children:
                helper(child, level + 1)
        res = []
        helper(root, level=0)
        return res
# @lc code=end
