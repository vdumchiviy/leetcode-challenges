class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        29. Divide Two Integers using school column method


        Given two integers dividend and divisor, divide two integers without
        using multiplication, division, and mod operator.
        Return the quotient after dividing dividend by divisor.

        The integer division should truncate toward zero, which means losing
        its fractional part. For example,
        truncate(8.345) = 8 and truncate(-2.7335) = -2.

        Note: Assume we are dealing with an environment that could only store
         integers within the 32-bit signed integer range:
        [−2**31, 2**31 − 1]. For this problem, assume that your function
        returns 2**31 − 1 when the division result overflows.

        Example 1: Input: dividend = 10, divisor = 3 Output: 3
        Explanation: 10/3 = truncate(3.33333..) = 3.
        Example 2: Input: dividend = 7, divisor = -3 Output: -2
        Explanation: 7/-3 = truncate(-2.33333..) = -2.
        Example 3: Input: dividend = 0, divisor = 1 Output: 0
        Example 4: Input: dividend = 1, divisor = 1 Output: 1


        Constraints:
        (-2**31) <= dividend, divisor <= (2**31) - 1
        divisor != 0        
        '''

        # if dividend == 0:
        #     return dividend

        d1 = abs(dividend)
        d2 = abs(divisor)
        overflow_up = 2147483647
        overflow_down = -2147483648
        # if d1 < d2:
        #     return 0

        sign = (1 if (dividend < 0 and divisor < 0) or (
            dividend > 0 and divisor > 0) else -1)
        # if divisor == 1:
        #     return overflow_up if sign > 0 and dividend >= overflow_up \
        #         else overflow_down if sign < 0 and dividend <= overflow_down \
        #         else d1 if sign > 0 \
        #         else -d1
        # if divisor == -1:
        #     return overflow_up if sign > 0 and d1 >= overflow_up \
        #         else overflow_down if sign < 0 and -dividend <= overflow_down \
        #         else d1 if sign > 0 \
        #         else -d1
        d1 = str(d1)
        pos = 0
        remains = 0
        result = ""
        while pos < len(d1):
            if int(str(remains) + d1[pos]) < d2:
                remains = int(str(remains) + d1[pos])
                result += "0"
            else:
                sub_d1 = int(str(remains) + d1[pos])
                new_value = 0
                multiplier = 0
                while new_value < sub_d1:
                    if new_value + d2 > sub_d1:
                        break
                    new_value += d2
                    multiplier += 1
                result += str(multiplier)
                remains = sub_d1 - new_value
            pos += 1
        multiplier = int(result)
        return overflow_up if sign > 0 and multiplier >= overflow_up \
            else overflow_down if sign < 0 and multiplier >= abs(overflow_down) \
            else multiplier if sign > 0 \
            else -multiplier

    def divide_minus(self, dividend: int, divisor: int) -> int:
        '''
        29. Divide Two Integers using minusing

        Given two integers dividend and divisor, divide two integers without
        using multiplication, division, and mod operator.
        Return the quotient after dividing dividend by divisor.

        The integer division should truncate toward zero, which means losing
        its fractional part. For example,
        truncate(8.345) = 8 and truncate(-2.7335) = -2.

        Note: Assume we are dealing with an environment that could only store
         integers within the 32-bit signed integer range:
        [−2**31, 2**31 − 1]. For this problem, assume that your function
        returns 2**31 − 1 when the division result overflows.

        Example 1: Input: dividend = 10, divisor = 3 Output: 3
        Explanation: 10/3 = truncate(3.33333..) = 3.
        Example 2: Input: dividend = 7, divisor = -3 Output: -2
        Explanation: 7/-3 = truncate(-2.33333..) = -2.
        Example 3: Input: dividend = 0, divisor = 1 Output: 0
        Example 4: Input: dividend = 1, divisor = 1 Output: 1


        Constraints:
        (-2**31) <= dividend, divisor <= (2**31) - 1
        divisor != 0'''

        if dividend == 0:
            return dividend
        d1 = abs(dividend)
        d2 = abs(divisor)
        overflow_up = 2147483647
        overflow_down = -2147483648
        if d1 < d2:
            return 0

        multiplier = 0
        new_value = 0
        sign = (1 if (dividend < 0 and divisor < 0) or (
            dividend > 0 and divisor > 0) else -1)
        if divisor == 1:
            return overflow_up if sign > 0 and dividend >= overflow_up \
                else overflow_down if sign < 0 and dividend <= overflow_down \
                else d1 if sign > 0 \
                else -d1
        if divisor == -1:
            return overflow_up if sign > 0 and d1 >= overflow_up \
                else overflow_down if sign < 0 and -dividend <= overflow_down \
                else d1 if sign > 0 \
                else -d1

        while new_value < d1:
            new_value += d2
            if new_value > d1:
                break
            multiplier += 1

        # print(multiplier, sign)
        # return multiplier if sign > 0 else -multiplier
        return overflow_up if sign > 0 and multiplier >= overflow_up \
            else overflow_down if sign < 0 and multiplier >= abs(overflow_down) \
            else multiplier if sign > 0 \
            else -multiplier


solution = Solution()
assert solution.divide(100, 200) == 0
assert solution.divide(-100, -3) == 33
assert solution.divide(2147483647, 2) == 1073741823
assert solution.divide(1234, -1) == -1234
assert solution.divide(0, 1) == 0
assert solution.divide(1, 1) == 1
assert solution.divide(-1234, 1) == -1234
assert solution.divide(4, 2) == 2
assert solution.divide(10, 3) == 3
assert solution.divide(7, -3) == -2
assert solution.divide(-1234, -1) == 1234
assert solution.divide(7777777777, -1) == -2147483648
assert solution.divide(7777777777, 1) == 2147483647
assert solution.divide(2147483647*3, 2) == 2147483647

assert solution.divide(2147483648, 1) == 2147483647
assert solution.divide(-2147483648, 1) == -2147483648
assert solution.divide(2147483647, -1) == -2147483647
assert solution.divide(-2147483648, -1) == 2147483647
assert solution.divide(-100, 3) == -33
assert solution.divide(100, -3) == -33
assert solution.divide(100, 3) == 33
