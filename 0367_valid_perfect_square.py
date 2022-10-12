'''
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which 
returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 0
        right = num
        med = right - (right-left) // 2
        while left < right:
            expected = med * med
            if expected == num:
                break
            if expected > num:
                right = med
            else:
                left = med
            med = right - (right-left) // 2
            if left == med or right == med:
                break
        return med * med == num


sol = Solution()

assert sol.isPerfectSquare(16) is True
assert sol.isPerfectSquare(14) is False
assert sol.isPerfectSquare(1) is True
assert sol.isPerfectSquare(2) is False
assert sol.isPerfectSquare(9) is True
