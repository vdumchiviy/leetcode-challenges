'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_val = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                try:
                    if check_val[ch] != stack.pop():
                        return False
                except Exception:
                    return False
        return False if len(stack) > 0 else True


        


sol = Solution()
assert sol.isValid("()") is True
assert sol.isValid("()[]{}") is True
assert sol.isValid("(]") is False
# assert sol.isValid() is
