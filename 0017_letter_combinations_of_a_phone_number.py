class Solution:
    def letterCombinations(self, digits: str):
        def get_symbols(phonepad, digit):
            x = 0
            length = len(phonepad[digit])
            while x < length:
                yield phonepad[digit][x]
                x += 1

        def recurse_digit(phonepad, digs, sub_result, result):
            if len(digs) == 1:
                for letter in get_symbols(phonepad, digs[0]):
                    result.append(sub_result + letter)
                return
            for letter in get_symbols(phonepad, digs[0]):
                recurse_digit(phonepad, digs[1:], sub_result+letter, result)
        if len(digits) == 0:
            return []
        result = list()
        phonepad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 1:
            return [letter for letter in get_symbols(phonepad, digits[0])]
            
        for letter in get_symbols(phonepad, digits[0]):
            recurse_digit(phonepad, digits[1:], letter, result)
        return result

    def letterCombinations_direct(self, digits: str):  # -> List[str]:
        '''17. Letter Combinations of a Phone Number
        Medium

        Given a string containing digits from 2-9 inclusive, return all possible letter combinations
        that the number could represent. Return the answer in any order.

        A mapping of digit to letters (just like on the telephone buttons) is given below.
        Note that 1 does not map to any letters.
        '''
        def get_symbols(phonepad, digit):
            x = 0
            length = len(phonepad[digit])
            while x < length:
                yield phonepad[digit][x]
                x += 1

        def recurse_call(start_code, multiplier, digits):
            if len(digits) == 1:
                return [digits]

            result_list = list()
            for d in digits:
                z = recurse_call(start_code, multiplier, digits[1:])
                for item in z:
                    result_list.append([d] + [item])
            return result_list

            # for x in get_symbols(start_code, multiplier, int(d)):
            #     recurse_call(start_code, multiplier, digits[1:])

        phonepad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 2:
            result = [f"{a}{b}" for a in get_symbols(phonepad, digits[0])
                      for b in get_symbols(phonepad, digits[1])]
        elif len(digits) == 3:
            result = [f"{a}{b}{c}" for a in get_symbols(phonepad, digits[0])
                      for b in get_symbols(phonepad, digits[1])
                      for c in get_symbols(phonepad, digits[2])]
        elif len(digits) == 4:
            result = [f"{a}{b}{c}{d}" for a in get_symbols(phonepad, digits[0])
                      for b in get_symbols(phonepad, digits[1])
                      for c in get_symbols(phonepad, digits[2])
                      for d in get_symbols(phonepad, digits[3])]
        elif len(digits) == 1:
            result = [f"{a}" for a in get_symbols(phonepad, digits[0])]
        elif len(digits) == 0:
            result = []

        print(result)

        return result


solution = Solution()
# assert solution.letterCombinations(
#     "23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert solution.letterCombinations("") == []
assert solution.letterCombinations("2") == ["a", "b", "c"]
assert solution.letterCombinations("7") == ["p", "q", "r", "s"]
# assert solution.letterCombinations() ==
# assert solution.letterCombinations() ==
# assert solution.letterCombinations() ==
# assert solution.letterCombinations() ==
# assert solution.letterCombinations() ==
