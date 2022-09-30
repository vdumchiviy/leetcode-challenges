'''
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is 
the same as the original string.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        result = ""

        for left in range(len(s)-1):
            position = len(s) - 1
            if position - left <= len(result):
                break
            while position > left or position != -1:
                position = s.rfind(s[left], left, position+1)
                if position == -1 or position == left:
                    break
                if position == len(s):
                    sl = s[left:]
                else:
                    sl = s[left:position + 1]
                position -= 1
                if sl == sl[::-1] and len(sl) > len(result):
                    result = sl
                    break

        return s[0] if result == "" else result


sol = Solution()
assert sol.longestPalindrome("abcdbab") == "bab"
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("babad") == "bab"
assert sol.longestPalindrome("bababad") == "babab"
assert sol.longestPalindrome("babababd") == "bababab"
assert sol.longestPalindrome("a") == "a"
assert sol.longestPalindrome("ab") == "a"
s = "tktneonoubkxgfhybavrfnetlxgtkelsoeeuznssntcleenqgiboexflfvlfiapqjbcwyenmfnmxcbcjscucqhwuqfzvvkdxrtxzhjdvsjawcwffoglhkxvyxaninlswyjcfvdwfkqheidwprtjaaqzqgloctafkuasubqqeacdpmtfzokccmnslnklxyvfitbfbdjrlzhkhnturfkimghcnngvdhbehewzzyfsbsactkrfabkhaavryubckkrqbqcbenqpeykyawzkctswaczbjtzeyteftsjklrtchxggsslscypkuilhbitsjwzsvwmqahxkmghigdtuqehjkqswchkrolcloxnkqocyjeorkwjmbevwijmqfhtmolspqcqshafjuxcheckguzxvapfivznkzdkzwnvlquzrbkhvmpdclrettjrxinbbvlwtsyepestvwjfiekjaqphfrhiifrplokslzaxmlwafrrfawlmxazlskolprfiihrfhpqajkeifjwvtsepeystwlvbbnixrjtterlcdpmvhkbrzuqlvnwzkdzknzvifpavxzugkcehcxujfahsqcqpslomthfqmjiwvebmjwkroejycoqknxolclorkhcwsqkjhequtdgihgmkxhaqmwvszwjstibhliukpycslssggxhctrlkjstfetyeztjbzcawstckzwaykyepqnebcqbqrkkcbuyrvaahkbafrktcasbsfyzzwehebhdvgnnchgmikfrutnhkhzlrjdbfbtifvyxlknlsnmcckozftmpdcaeqqbusaukfatcolgqzqaajtrpwdiehqkfwdvfcjywslninaxyvxkhlgoffwcwajsvdjhzxtrxdkvvzfquwhqcucsjcbcxmnfmneywcbjqpaiflvflfxeobigqneelctnssnzueeoslektgxltenfrvabyhfgxkbuonoentkt"
# print(sol.longestPalindrome(s))
assert sol.longestPalindrome(s) == s
