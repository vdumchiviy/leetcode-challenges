'''
88. Merge Sorted Array
Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored 
inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. 
The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10**9 <= nums1[i], nums2[j] <= 10**9
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return

        pos1 = 0
        pos2 = 0
        while pos1 < m + n or pos2 < n:
            if pos1 < m + pos2 and pos2 < n:
                if nums2[pos2] < nums1[pos1]:
                    nums1.insert(pos1, nums2[pos2])
                    pos2 = min(pos2 + 1, n)
                else:
                    pos1 = min(pos1 + 1, m + pos2)
            else:
                while pos2 < n:
                    nums1[pos1] = nums2[pos2]
                    pos1 += 1
                    pos2 += 1
                break
        del nums1[n+m:]


sol = Solution()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
expected = [1, 2, 2, 3, 5, 6]
sol.merge(nums1, m, nums2, n)
print(f'nums1={nums1}, expected={expected}')
assert nums1 == expected

nums1 = [1]
m = 1
nums2 = []
n = 0
expected = [1]
sol.merge(nums1, m, nums2, n)
print(f'nums1={nums1}, expected={expected}')
assert nums1 == expected

nums1 = []
m = 0
nums2 = [1]
n = 1
expected = [1]
sol.merge(nums1, m, nums2, n)
print(f'nums1={nums1}, expected={expected}')
assert nums1 == expected

nums1 = [1, 3, 8, 0, 0, 0]
m = 3
nums2 = [5, 6, 9]
n = 3
expected = [1, 3, 5, 6, 8, 9]
sol.merge(nums1, m, nums2, n)
print(f'nums1={nums1}, expected={expected}')
assert nums1 == expected


nums1 = [-11, -9, -8, 0, 0, 0]
m = 3
nums2 = [-55, -45, -9]
n = 3
expected = [-55, -45, -11, -9, -9, -8]
sol.merge(nums1, m, nums2, n)
print(f'nums1={nums1}, expected={expected}')
assert nums1 == expected
