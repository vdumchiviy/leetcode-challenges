'''
67. Add Binary
Easy

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10**4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        right_a = len(a)-1
        right_b = len(b)-1
        result = ""
        additional = 0
        while right_a >= 0 or right_b >= 0 or additional == 1:
            xa = 0
            xb = 0
            if right_a >= 0:
                xa = int(a[right_a])
                right_a -= 1
            if right_b >= 0:
                xb = int(b[right_b])
                right_b -= 1            
            x = xa + xb + additional
            if x == 0 or x == 1:
                result = str(x) + result
                additional = 0
            elif x == 2:
                result = "0" + result
                additional = 1
            elif x == 3:
                result = "1" + result
                additional = 1
        return result


sol = Solution()
assert sol.addBinary("1", "1") == "10"
assert sol.addBinary("1","0") == "1"
assert sol.addBinary("0","0") == "0"
assert sol.addBinary("11", "1") == "100"