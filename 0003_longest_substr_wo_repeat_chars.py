'''
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s: int = len(s)
        if len_s == 0:
            return 0

        result = 1
        for start in range(len_s):
            sub_string = ""
            if start < len_s - 1:
                for current in range(len_s - start):
                    if s[start + current] not in sub_string:
                        sub_string += s[start + current]
                    else:
                        break
                result = max(result, len(sub_string))
            if len(sub_string) == len_s:
                return len_s

        return result


solution = Solution()
assert solution.lengthOfLongestSubstring("aab") == 2
assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
assert solution.lengthOfLongestSubstring("abscdefgh") == 9
# assert solution.lengthOfLongestSubstring("") == 3
