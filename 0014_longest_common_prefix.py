'''
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

from typing import List


class Solution:
    def longestCommonPrefix_old(self, strs: List[str]) -> str:
        row_count = len(strs)
        if row_count == 1:
            return strs[0]

        position = 0
        result = ""
        while True:
            try:
                ch = strs[0][position]
                for row in range(row_count-1):
                    if strs[row+1][position] != ch:
                        return result
                result += ch
                position += 1
            except Exception:
                return result

    def longestCommonPrefix(self, strs: List[str]) -> str:

        z1 = "".join([x[0] if len(set(x)) == 1 else "-" for x in zip(*strs)])
        return z1 if z1.find('-') == -1 else z1[:z1.find('-')]
    


# print(list(zip(list(x) for x in ["flower","flow","flight"])))
# print()
# z1 = zip([list(x) for x in ["flower", "flow", "flight"]])
# print(list(z1))
strs=["dog", "dog", "dog"]
minimum = min([len(x) for x in strs])
z1 = ''.join([x[0] if len(set(x)) == 1 else "-" for x in zip(*strs)])
print(z1 if z1.find('-') == -1 else z1[:z1.find('-')])
print(z1)
print(z1.find('-'))
print(z1[:z1.find('-')])

sol = Solution()

assert sol.longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(strs=["dog", "racecar", "car"]) == ""

assert sol.longestCommonPrefix(strs=["dog", "", "car"]) == ""
assert sol.longestCommonPrefix(strs=["", "", ""]) == ""
assert sol.longestCommonPrefix(strs=["dog", "dog", "dog"]) == "dog"
