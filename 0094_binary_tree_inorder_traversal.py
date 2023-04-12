"""
94. Binary Tree Inorder Traversal
Companies
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def deep(root: Optional[TreeNode]):
            if root is None:
                return

            deep(root.left)
            self.result.append(root.val)
            deep(root.right)

        self.result = []
        deep(root)
        print(self.result)
        return self.result

    def create_balanced_btree_from_sorted_list(self, nums: List[int]) -> TreeNode:
        # Just for close the branch with no leaves at all
        if len(nums) == 0:
            return None

        # if only 1 value = it means that there are no leaves
        if len(nums) == 1:
            return TreeNode(nums[0])

        # MAIN: find the middle value in a list.
        # Left side for the .left, right side for the .right.
        # middle values as a val of the Node
        i = int(len(nums) / 2)
        return TreeNode(
            nums[i],
            self.create_balanced_btree_from_sorted_list(nums[:i]),
            self.create_balanced_btree_from_sorted_list(nums[i+1:])
        )


sol = Solution()
tree = TreeNode(
    1,
    None,
    TreeNode(
        2,
        TreeNode(3),
        None
    )
)
assert sol.inorderTraversal(tree) == [1, 3, 2]
assert sol.inorderTraversal(None) == []
