'''
111. Minimum Depth of Binary Tree
Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node 
down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:
3--20--7
|   |
|   15
9
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
2--3--4--5--6
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 10**5].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
from cmath import inf
from ctypes import pointer
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def deep(point: TreeNode, counter: int):
            if point.left is None and point.right is None:
                self.deep_min = min(self.deep_min, counter+1)
                return
            if counter + 1 >= self.deep_min:
                return
            if point.left is not None:
                deep(point.left, counter+1)
            if point.right is not None:
                deep(point.right, counter+1)

            
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        self.deep_min = float(inf)
        if root.left is not None:
            deep(root.left, 0)
        if root.right is not None:
            deep(root.right, 0)
            
        return self.deep_min+1



sol = Solution()

# [3,9,20,null,null,15,7]
head = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert sol.minDepth(head) == 2

# [1,null,2]
head = TreeNode(1, None, TreeNode(2))
assert sol.minDepth(head) == 2

# [1,null,null]
head = TreeNode(1, None, None)
assert sol.minDepth(head) == 1

# []
assert sol.minDepth(None) == 0

# [1]
assert sol.minDepth(TreeNode(1)) == 1

# [2,null,3,null,4,null,5,null,6]
head = (TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6))))))
assert sol.minDepth(head) == 5
