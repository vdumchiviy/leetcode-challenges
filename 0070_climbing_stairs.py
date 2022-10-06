'''
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb 
to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 2
        prev_prev = 1
        len_n = n - 1 - 2
        result = prev_prev + prev
        for x in range(len_n):
            prev_prev, prev = prev, result
            result = prev_prev + prev
        return result


sol = Solution()

assert sol.climbStairs(1) == 1
assert sol.climbStairs(2) == 2
assert sol.climbStairs(3) == (2)+(1)
assert sol.climbStairs(4) == (2+1)+(2)
assert sol.climbStairs(5) == ((2+1)+(2)) + ((2)+(1))

