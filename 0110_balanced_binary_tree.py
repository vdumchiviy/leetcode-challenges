'''
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height 
by no more than 1.

Example 1:
3--20--7
|   |
|   15
9
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
1--2
|
2--3
|
3--4
|
4
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10**4 <= Node.val <= 10**4
'''

# Definition for a binary tree node.

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def deep_balance(
            point: Optional[TreeNode]
        ) -> Tuple[bool, int]:
            if point is None:
                return True, 0

            is_left_balanced, left_high = deep_balance(point.left)
            is_right_balanced, right_high = deep_balance(point.right)
            
            # main condition: if somewhere unbalanced, then we "push up" False to the top
            is_bal = (is_left_balanced and is_right_balanced) and abs(left_high - right_high) <= 1
            high = max(left_high, right_high) + 1
            return is_bal, high

        if root is None:
            return True

        balanced, high = deep_balance(root)
        return balanced


sol = Solution()

# [3,9,20,null,null,15,7]
head = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert sol.isBalanced(head) is True

# [1,2,2,3,3,null,null,4,4]
head = TreeNode(
    1,
    TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
    TreeNode(2)
)
assert sol.isBalanced(head) is False

assert sol.isBalanced(None) is True
