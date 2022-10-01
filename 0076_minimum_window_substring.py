'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates)
 is included in the window. 
 
 If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 10 ** 5
s and t consist of uppercase and lowercase English letters (code no more than 123)

>>print(ord('A'), ord('Z'), ord('a'), ord('z')) 
65 90 97 122

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return ""

        s_hash = [0] * 123
        t_hash = [0] * 123
        result_window_len = 10 ** 5
        result_left_pos = -1
        left = 0
        chars_count = 0
        for x in t:
            t_hash[ord(x)] += 1

        for s_pos in range(s_len):
            s_char_hash = ord(s[s_pos])
            s_hash[s_char_hash] += 1
            if s_hash[s_char_hash] <= t_hash[s_char_hash]:
                chars_count += 1

            if chars_count == t_len:
                left_hash = ord(s[left])
                while (s_hash[left_hash] > t_hash[left_hash] or t_hash[left_hash] == 0):
                    if s_hash[left_hash] > t_hash[left_hash]:
                        s_hash[left_hash] = s_hash[left_hash] - 1
                    left += 1
                    left_hash = ord(s[left])

                current_window_len = s_pos - left + 1
                if current_window_len < result_window_len:
                    result_window_len = current_window_len
                    result_left_pos = left

        return "" if result_left_pos == -1 else s[result_left_pos:result_left_pos + result_window_len]


sol = Solution()
assert sol.minWindow(s="AADzOBECOzDEBANC", t="ABC") == "BANC"
assert sol.minWindow(s="a", t="a") == "a"
assert sol.minWindow(s="a", t="aa") == ""
