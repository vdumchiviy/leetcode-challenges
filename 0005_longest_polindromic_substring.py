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

    def is_pol(self, substr: str) -> bool:
        return True if substr == substr[::-1] else False

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        result = ""
        for left in range(len(s)-1):
            position = left
            while position < len(s) or position != -1:
                position = s.find(s[left], position + 1)
                if position == -1:
                    break
                sl = s[left:] \
                    if position == len(s) \
                    else s[left:position + 1]

                if self.is_pol(sl) and len(sl) > len(result):
                    result = sl
                
                position += 1
                
        return s[0] if result == "" else result


sol = Solution()
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("babad") == "bab"
assert sol.longestPalindrome("bababad") == "babab"
assert sol.longestPalindrome("babababd") == "bababab"
assert sol.longestPalindrome("abcdbab") == "bab"
assert sol.longestPalindrome("a") == "a"
assert sol.longestPalindrome("ab") == "a"
s = "tktneonoubkxgfhybavrfnetlxgtkelsoeeuznssntcleenqgiboexflfvlfiapqjbcwyenmfnmxcbcjscucqhwuqfzvvkdxrtxzhjdvsjawcwffoglhkxvyxaninlswyjcfvdwfkqheidwprtjaaqzqgloctafkuasubqqeacdpmtfzokccmnslnklxyvfitbfbdjrlzhkhnturfkimghcnngvdhbehewzzyfsbsactkrfabkhaavryubckkrqbqcbenqpeykyawzkctswaczbjtzeyteftsjklrtchxggsslscypkuilhbitsjwzsvwmqahxkmghigdtuqehjkqswchkrolcloxnkqocyjeorkwjmbevwijmqfhtmolspqcqshafjuxcheckguzxvapfivznkzdkzwnvlquzrbkhvmpdclrettjrxinbbvlwtsyepestvwjfiekjaqphfrhiifrplokslzaxmlwafrrfawlmxazlskolprfiihrfhpqajkeifjwvtsepeystwlvbbnixrjtterlcdpmvhkbrzuqlvnwzkdzknzvifpavxzugkcehcxujfahsqcqpslomthfqmjiwvebmjwkroejycoqknxolclorkhcwsqkjhequtdgihgmkxhaqmwvszwjstibhliukpycslssggxhctrlkjstfetyeztjbzcawstckzwaykyepqnebcqbqrkkcbuyrvaahkbafrktcasbsfyzzwehebhdvgnnchgmikfrutnhkhzlrjdbfbtifvyxlknlsnmcckozftmpdcaeqqbusaukfatcolgqzqaajtrpwdiehqkfwdvfcjywslninaxyvxkhlgoffwcwajsvdjhzxtrxdkvvzfquwhqcucsjcbcxmnfmneywcbjqpaiflvflfxeobigqneelctnssnzueeoslektgxltenfrvabyhfgxkbuonoentkt"
# print(sol.longestPalindrome(s))
assert sol.longestPalindrome(s) == s
