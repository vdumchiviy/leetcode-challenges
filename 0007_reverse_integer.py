class Solution:

    def reverse(self, x: int) -> int:
        """Given a signed 32-bit integer x, return x with its digits reversed. 
        If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31-1], then return 0.
        !!! Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
        Examples: 
        Input: x = 123  Output: 321
        Input: x = -123 Output: -321
        Input: x = 120  Output: 21
        Input: x = 0    Output: 0

        Constraints:  -2^31 <= x <= 2^31 - 1
        Args:
            x (int): [initial value]

        Returns:
            int: [reversed initial value]
        """
        max_value = str(2**31-1)
        min_value = str(-(2**31))
        if x < 0:
            s = '-' + str(abs(x))[::-1]
            print(f"input {x} constraint {min_value} <= {s} <= {max_value}")
            if len(s) > len(min_value):
                result = 0
            elif (len(s) < len(min_value)) or (s == min_value):
                result = s
            else:
                list_values = [min_value, s]
                list_values.sort()
                if s == list_values[1]:
                    result = 0
                else:
                    result = s
        else:
            s = str(x)[::-1]
            print(f"input {x} constraint {min_value} <= {s} <= {max_value}")
            if len(s) > len(max_value):
                result = 0
            elif len(s) < len(max_value) or s == max_value:
                result = s
            else:
                list_values = [max_value, s]
                list_values.sort()
                if s == list_values[1]:
                    result = 0
                else:
                    result = s
        return int(result)


# print(2**32)
leetcode_test = Solution()
test = int('-' + str(2 ** 31)[::-1])

print(leetcode_test.reverse(test))
