"""
137. Single Number II
Medium

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
 
1 <= nums.length <= 3 * 10**4
-2**31 <= nums[i] <= 2**31 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""
from typing import List
import operator


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result1 = nums[0]
        result2 = nums[0]
        for n in nums[1:]:
            result1 = operator.xor(operator.xor(result1, n), n)

        return result1


sol = Solution()

nums = [2, 2, 3, 2]
assert sol.singleNumber(nums) == 3
