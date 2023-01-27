"""
680. Valid Palindrome II
Easy
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 10**5
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        occured = 0
        left_occured = -1
        right_occured = -1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue

            if occured == 0:
                occured = 1
                left_occured = left
                right_occured = right
                left += 1
                continue
            elif occured == 1:
                occured = 2
                left = left_occured
                right = right_occured
                right -= 1
                continue
            else:
                return False

        return True


sol = Solution()

s = "aba"
assert sol.validPalindrome(s) is True

s = "abca"
assert sol.validPalindrome(s) is True

s = "abc"
assert sol.validPalindrome(s) is False

s = "axybxa"
assert sol.validPalindrome(s) is True

s = "axbyxa"
assert sol.validPalindrome(s) is True


s = "axyxba"
assert sol.validPalindrome(s) is True

s = "abxyxa"
assert sol.validPalindrome(s) is True
