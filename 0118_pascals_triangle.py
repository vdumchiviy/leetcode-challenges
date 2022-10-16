'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly 
above it as shown:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

 

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
'''


from operator import sub
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 0 = 1, 1 = 0+1, 2 = 1+2, 3=2+3
        result = list()
        result.append([1])
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result

        for line in range(3, numRows+1):
            sub_list = [1]
            for pos in range(1, line//2):
                sub_list.append(result[line-2][pos]+result[line-2][pos-1])
            if line % 2 == 0:
                sub_list[:] = sub_list + sub_list[::-1]
            else:
                pos = line//2
                sub_list.append(result[line-2][pos] + result[line-2][pos-1])
                sub_list[:] = sub_list + sub_list[:pos:][::-1]
            result.append(sub_list)

        return result


sol = Solution()

assert sol.generate(5) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]

assert sol.generate(7) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1]
]
