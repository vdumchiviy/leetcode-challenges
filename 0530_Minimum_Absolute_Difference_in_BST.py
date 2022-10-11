'''
530. Minimum Absolute Difference in BST
Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute difference 
between the values of any two different nodes in the tree.

 

Example 1:
4--6
|
2--3
|
1
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
1--48--49
|   |
|   12
0
Input: root = [1,0,48,null,null,12,49]
Output: 1
 
Example 3
1--48--49
|  |
|  12
0
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10**4].
0 <= Node.val <= 10**5
'''

# Definition for a binary tree node.
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def node_cycle(point: Optional[TreeNode]):
            def deep(point: Optional[TreeNode], diff):
                if point.left is None and point.right is None:
                    self.minimum = min(self.minimum, abs(diff))
                    return diff
                if diff != 0:
                    self.minimum = min(self.minimum, abs(diff))
                if point.left is not None:
                    deep(point.left, diff + point.val - point.left.val)
                if point.right is not None:
                    deep(point.right, diff + point.val - point.right.val)

            if point is None:
                return
            if point.left is None and point.right is None:
                return self.minimum
            deep(point, 0)
            node_cycle(point.left)
            node_cycle(point.right)

        self.minimum = float(inf)
        node_cycle(root)
        return self.minimum


sol = Solution()

# [600,424,612,null,499,null,689]
root = TreeNode(
    600,
    TreeNode(424, None, TreeNode(499)),
    TreeNode(612, None, TreeNode(689))
)
assert sol.getMinimumDifference(root) == 12


# [543,384,652,null,445,null,699]
root = TreeNode(
    543,
    TreeNode(384, None, TreeNode(445)),
    TreeNode(652, None, TreeNode(699))
)
assert sol.getMinimumDifference(root) == 47


# [4,2,6,1,3]
root = TreeNode(
    4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6)
)
assert sol.getMinimumDifference(root) == 1

# Example 3
# 1--48--49
# |  |
# |  12
# 0
# Input: root = [1,0,48,null,null,12,49]
root = TreeNode(
    1,
    TreeNode(0),
    TreeNode(48, TreeNode(12), TreeNode(49))
)
assert sol.getMinimumDifference(root) == 1

# [236,104,701,null,227,null,911]
# 236--701--911
# |
# |
# 104-227
root = TreeNode(
    236,
    TreeNode(104, None, TreeNode(227)),
    TreeNode(701, None, TreeNode(911))
)
assert sol.getMinimumDifference(root) == 9


root = TreeNode(
    236,
    TreeNode(
        104,
        TreeNode(100),
        TreeNode(
            227,
            TreeNode(220),
            TreeNode(
                230,
                None,
                TreeNode(235)
            )
        )
    ),
    TreeNode(701, None, TreeNode(911))
)
assert sol.getMinimumDifference(root) == 1
