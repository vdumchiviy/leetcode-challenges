'''
69. Sqrt(x)
Easy

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, 
such as pow(x, 0.5) or x ** 0.5.

 

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 
2 is returned.
 

Constraints:
0 <= x <= 2**31 - 1
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x

        left = 0
        right = x
        med = right - (right-left) / 2
        int_med = int(med)
        while not (int_med * int_med >= x and (int_med-1)*(int_med-1) < x):
            if int_med * int_med >= x:
                right = med
            else:
                left = med
            med = right - (right - left) / 2
            int_med = int(med)
        return int_med if int_med * int_med == x else int(med-1)


sol = Solution()

assert sol.mySqrt(4) == 2
assert sol.mySqrt(8) == 2
assert sol.mySqrt(1) == 1
assert sol.mySqrt(69696) == 264
assert sol.mySqrt(777777) == 881
assert sol.mySqrt(123456789) == 11111
