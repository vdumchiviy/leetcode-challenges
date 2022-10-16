'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1


Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]


Constraints:
0 <= rowIndex <= 33
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''
import operator
from functools import reduce
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fact(num):
            if num in [0, 1, 2]:
                return num
            return int(reduce(operator.mul, [i for i in range(2, num + 1)]))

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        if rowIndex == 2:
            return [1, 2, 1]

        result = [1, rowIndex]
        for pos in range(2, (rowIndex+1)//2):
            result.append(int(fact(rowIndex)/(fact(pos)*fact(rowIndex-pos))))
        if rowIndex % 2 == 0:
            pos = rowIndex // 2
            result.append(int(fact(rowIndex)/(fact(pos)*fact(rowIndex-pos))))
            result[:] = result + result[:pos][::-1]
        else:
            result[:] = result + result[::-1]

        return result


sol = Solution()

assert sol.getRow(0) == [1]
assert sol.getRow(1) == [1, 1]
assert sol.getRow(3) == [1, 3, 3, 1]
assert sol.getRow(4) == [1, 4, 6, 4, 1]
assert sol.getRow(5) == [1, 5, 10, 10, 5, 1]
assert sol.getRow(6) == [1, 6, 15, 20, 15, 6, 1]
