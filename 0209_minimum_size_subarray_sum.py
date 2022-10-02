'''
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is GREATER than OR EQUAL to target. 
If there is no such subarray, return 0 instead.

 

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:
1 <= target <= 10**9
1 <= nums.length <= 10**5
1 <= nums[i] <= 10**4
'''
import json
from typing import List


class Solution_old:
    def deep(self, target, nums, position) -> int:
        # this is the end of the nums, but target didn't found
        if position >= len(nums):
            return -1
            
        # or current value more than target
        if nums[position] >= target:
            return position
        # target was found, returns current position
        if nums[position] == target:
            return position

        return self.deep(
            target=target - nums[position],
            nums=nums,
            position=position + 1
        )

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        result = (10**5)+1  # more than maximum based on Constraint
        for x in range(len(nums)):
            if nums[x] >= target:
                return 1
            if nums[x] == target:
                return 1

            # current digit less than target
            position = self.deep(
                target=target-nums[x],
                nums=nums,
                position=x + 1
            )
            if position > -1:
                result = min(result, position - x + 1)

        return 0 if result == (10**5)+1 else result

class Solution_old2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        result = (10**5)+1  # more than maximum based on Constraint
        left = 0
        right = 0
        to_target = 0
        len_nums = len(nums)
        while left < len_nums:
            if right == len_nums:
                left += 1
                right = left
                to_target = 0
                continue
                                
            to_target = to_target + nums[right]
            if to_target >= target:
                result = min(result, right - left + 1)
                if result == 1:
                    return result
                left += 1
                right = left
                to_target = 0
            else:
                right += 1
        print(f"result = {result}")
        return 0 if result == (10**5)+1 else result


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        result = (10**5)+1  # more than maximum based on Constraint
        left = 0
        right = 0
        to_target = 0
        len_nums = len(nums)

        while right < len_nums:

            while to_target < target and right < len_nums:
                to_target = to_target + nums[right]
                right += 1

            while to_target >= target and left < len_nums:
                result = min(result, right - left)
                if result == 1:
                    return result
                to_target = to_target - nums[left]
                left += 1

        return 0 if result == (10**5)+1 else result


sol = Solution()
with open("0209_minimum_size_subarray_sum.json") as f:
    data = json.load(f)
    for d in data["items"]:
        target = d["target"]
        nums = d["nums"]
        expected = d["expected"]
        actual = sol.minSubArrayLen(target=target, nums=nums)
        print(f"{actual}: {expected}")
        assert actual == expected  
