"""
204. Count Primes
Medium
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 10*6
    """

from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        cito = {key: True
                for key in range(2, n) if (key <= 2 or key % 2 != 0) and (key <= 5 or key % 5 != 0)
                }
        for current in range(3, n):
            quad_current = current * current
            if quad_current >= n:
                break
            
            mult = 0
            check_value = quad_current + current * mult
            while check_value < n:
                if (check_value % 2 == 0) or (check_value > 5 and check_value % 5 == 0):
                    pass
                elif cito.get(check_value, False):
                    del cito[check_value]
                mult += 1
                check_value = quad_current + current * mult
        return len(cito)      

    def countPrimes_v2(self, n: int) -> int:
        primes: list = [2]
        if n <= 2:
            return 0
        for current in range(3, n):
            # skip 6 of each 10 values
            if current % 2 == 0 or (current >= 10 and current % 5 == 0):
                continue
            else:
                # I check only until the prime value < sqrt(current)
                max_current_sqrt = int(sqrt(current))
                pos = 0
                flag = False
                while primes[pos] <= max_current_sqrt:
                    if current % primes[pos] == 0:
                        flag = True
                        break
                    pos += 1
                if not flag:
                    primes.append(current)
        return len(primes)

    def countPrimes_v1(self, n: int) -> int:
        primes: list = [2]
        if n <= 2:
            return 0
        current = 3
        while current < n:
            # if current couldn't devide without rest for all previous primes..
            if current % 2 != 0 and not any(filter(lambda prime_in_list: current % prime_in_list == 0, primes)):
                primes.append(current)
            current += 1

        return len(primes)


sol = Solution()

assert sol.countPrimes(5000000) == 348513
assert sol.countPrimes(499979) == 41537
assert sol.countPrimes(10) == 4
assert sol.countPrimes(30) == 10
assert sol.countPrimes(29) == 9
assert sol.countPrimes(0) == 0
assert sol.countPrimes(1) == 0
assert sol.countPrimes(2) == 0
assert sol.countPrimes(3) == 1
