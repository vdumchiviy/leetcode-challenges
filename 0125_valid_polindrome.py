"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 10**5
s consists only of printable ASCII characters.
    """


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


sol = Solution()

s = "A man, a plan, a canal: Panama"
assert sol.isPalindrome(s) is True

s = "race a car"
assert sol.isPalindrome(s) is False

s = " "
assert sol.isPalindrome(s) is True

s = "  "
assert sol.isPalindrome(s) is True

s = "   "
assert sol.isPalindrome(s) is True

s = "rrrrrrrrrr"
assert sol.isPalindrome(s) is True

s = "rrrrrrrrrrr"
assert sol.isPalindrome(s) is True

s = "rr"
assert sol.isPalindrome(s) is True
s = "rrr"
assert sol.isPalindrome(s) is True
s = "rar"
assert sol.isPalindrome(s) is True
s = "r.r"
assert sol.isPalindrome(s) is True
s = "r.r."
assert sol.isPalindrome(s) is True
s = ".r.r."
assert sol.isPalindrome(s) is True
s = "0P"
assert sol.isPalindrome(s) is False
