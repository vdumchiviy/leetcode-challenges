'''
43. Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert 
the inputs to integer directly.

 

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        right2 = len(num2) - 1
        result = 0
        while right2 >= 0:
            additional = 0
            preresult = ""
            right1 = len(num1) - 1
            while right1 >= 0 or additional != 0:
                x = 0
                if right1 >= 0:
                    x = int(num2[right2]) * int(num1[right1])
                    right1 -= 1
                x = x + additional
                preresult = str(x % 10) + preresult
                additional = x // 10
            result = result + int(preresult) * (10 ** (len(num2) - 1 - right2))
            right2 -= 1
        return str(result)


sol = Solution()

assert sol.multiply("123", "456") == "56088"
assert sol.multiply("11", "11") == "121"
assert sol.multiply("125698", "0") == "0"
assert sol.multiply("0", "0") == "0"
assert sol.multiply("0", "125") == "0"
assert sol.multiply("7", "12") == "84"