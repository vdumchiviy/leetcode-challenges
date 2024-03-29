'''
415. Add Strings
Easy
 
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library 
for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 10**4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        right1 = len(num1) - 1
        right2 = len(num2) - 1

        result = ""
        additional = 0
        while right1 >= 0 or right2 >= 0 or additional != 0:
            x1 = 0
            x2 = 0
            if right1 >= 0:
                x1 = int(num1[right1])
                right1 -= 1
            if right2 >= 0:
                x2 = int(num2[right2])
                right2 -= 1
            x = x1 + x2 + additional
            additional = x // 10
            result = str(x - additional*10) + result
        return result


sol = Solution()

assert sol.addStrings("11", "123") == "134"
assert sol.addStrings("456", "77") == "533"
assert sol.addStrings("0", "0") == "0"

        