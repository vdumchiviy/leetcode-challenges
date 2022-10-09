'''
977. Squares of a Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, return an array 
of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0 or len(nums) == 1:
            return [x**2 for x in nums]

        left = 0
        right = len(nums) - 1
        result = []
        while left != right:
            if abs(nums[left]) >= abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        result.append(nums[left] ** 2)
        return result[::-1]


sol = Solution()

assert sol.sortedSquares([0, 3, 10]) == [0, 9, 100]
assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sol.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
