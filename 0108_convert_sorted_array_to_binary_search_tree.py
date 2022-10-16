'''
108. Convert Sorted Array to Binary Search Tree
Easy

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth 
of the two subtrees of every node never differs by more than one.

 

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in a strictly increasing order.
'''


# Definition for a binary tree node.
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def balance_it(point: TreeNode):
            # point = 3 point.left = 2 point.left.left = 1
            # point = 3 point.left = 1 point.left.left = 0 point.left.right = 2
            if point.left.left is None and point.right.right is None:
                return
            point.left = point.left.left

        if len(nums) == 1:
            return TreeNode(nums[0])
        center = len(nums) // 2
        head = TreeNode(nums[center])

        point = head
        pos = center - 1
        while pos >= 0:
            point.left = TreeNode(nums[pos])
            point = point.left
            pos -= 1

        point = head
        pos = center + 1
        while pos < len(nums):
            point.right = TreeNode(nums[pos])
            point = point.right
            pos += 1

        return head



sol = Solution()


#  [0,-3,9,-10,null,5]
bst = TreeNode(
    0,
    TreeNode(-3, TreeNode(-10), None),
    TreeNode(5, None, TreeNode(5))
)
assert sol.sortedArrayToBST([-10, -3, 0, 5, 9]) == bst
