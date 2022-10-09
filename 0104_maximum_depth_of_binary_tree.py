'''
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

 

Example 1:
3--20--7
|   |
|   15
9

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
1--2

Input: root = [1,null,2]
Output: 2
 

Constraints:
The number of nodes in the tree is in the range [0, 10**4].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def deep(point: Optional[TreeNode], result: int):
            if point.left is None and point.right is None:
                self.DEEP_MAX = max(self.DEEP_MAX, result+1)
            
            if point.left is not None:
                deep(point.left, result + 1)
            if point.right is not None:
                deep(point.right, result + 1)
            return
        if root is None:
            return 0
        self.DEEP_MAX = 0
        if root.left is not None:
            deep(root.left, 0)
        if root.right is not None:
            deep(root.right, 0)
            
        return self.DEEP_MAX + 1                


sol = Solution()

# [3,9,20,null,null,15,7]
head = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert sol.maxDepth(head) == 3

# [1,null,2]
head = TreeNode(1, None, TreeNode(2))
assert sol.maxDepth(head) == 2

# [1,null,null]
head = TreeNode(1, None, None)
assert sol.maxDepth(head) == 1

#[]
assert sol.maxDepth(None) == 0

#[1]
assert sol.maxDepth(TreeNode(1)) == 1
