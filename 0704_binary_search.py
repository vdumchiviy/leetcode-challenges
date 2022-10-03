'''
704. Binary Search
Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) (!!!!!!) runtime complexity.

 

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 10**4
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 0 if target == nums[0] else -1
        
        left = 0
        right = len_nums - 1

        while left <= right:
            position = (left + right) // 2
            if nums[position] == target:
                return position
            
            if nums[position] > target:
                if position == right:
                    # avoid "1" problem (infinite cycle)                    
                    if right - left == 1:
                        right = left
                    else:
                        return -1
                else:
                    right = position
            elif nums[position] < target:
                if position == left:
                    # avoid "1" problem (infinite cycle)
                    if right - left == 1:
                        left = right
                    else:
                        return -1
                else:
                    left = position
        return -1

sol = Solution()
assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4

nums = [x for x in range(0, 1000001)]
assert sol.search(nums, 7000) == 7000
assert sol.search([-1, 0, 3, 5, 9, 12], -2) == -1
assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1

assert sol.search([-1, 0, 3, 5, 9, 12], -1) == 0
assert sol.search([-1, 0, 3, 5, 9, 12], 12) == 5
assert sol.search([-1, 0, 3, 5, 9, 12], 3) == 2
assert sol.search([-1, 0, 3, 5, 9, 12], 5) == 3

assert sol.search([-1, 0, 3, 5, 9, 12], -2) == -1
assert sol.search([-1, 0, 3, 5, 9, 12], 13) == -1
assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
assert sol.search([-1, 0, 3, 5, 9, 12], 4) == -1
assert sol.search([-1, 0, 3, 5, 9, 12], 7) == -1
assert sol.search([-1, 0, 3, 5, 9, 12], 11) == -1


