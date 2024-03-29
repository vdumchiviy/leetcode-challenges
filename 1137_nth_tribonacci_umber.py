'''
1137. N-th Tribonacci Number
Easy

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
 

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
 

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1

        prev3 = 0
        prev2 = 1
        prev1 = 1
        result = prev3 + prev2 + prev1
        for x in range(n - 1 - 2):
            prev3, prev2, prev1 = prev2, prev1, result
            result = prev3 + prev2 + prev1

        return result


sol = Solution()

assert sol.tribonacci(0) == 0
assert sol.tribonacci(1) == 1
assert sol.tribonacci(2) == 1
assert sol.tribonacci(3) == 2
assert sol.tribonacci(4) == 4
assert sol.tribonacci(5) == 7
assert sol.tribonacci(25) == 1389537
