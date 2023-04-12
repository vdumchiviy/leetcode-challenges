"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:
=================
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums contains distinct values sorted in ascending order.
-10**4 <= target <= 10**4
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        pos = int((left + right) / 2)
        while left != right:
            if target == nums[pos]:
                return pos
            elif target < nums[pos]:
                if right-left > 1:
                    right = pos
                else:
                    # avoid infinity cycling
                    right -= 1
            elif target > nums[pos]:
                if right-left > 1:
                    left = pos
                else:
                    # avoid infinity cycling
                    left += 1
            pos = int((left + right) / 2)

        if target <= nums[pos]:
            return pos
        else:
            return pos + 1


sol = Solution()

assert sol.searchInsert([1, 3, 5, 6], 5) == 2
assert sol.searchInsert([1, 3, 5, 6], 2) == 1
assert sol.searchInsert([1, 3, 5, 6], 7) == 4
assert sol.searchInsert([1, 3, 5, 6], 0) == 0
assert sol.searchInsert([1, 3, 5, 6], -1) == 0
assert sol.searchInsert([1, 3, 5, 6], 11) == 4
assert sol.searchInsert([1, 3, 5, 6], -11) == 0
assert sol.searchInsert([0], -1) == 0
assert sol.searchInsert([0], 1) == 1
assert sol.searchInsert([0], 0) == 0
