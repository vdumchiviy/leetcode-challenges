class Solution():
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        48. Rotate Image
        Medium

        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.
        Example 1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[7,4,1],[8,5,2],[9,6,3]]
        Example 2:
        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        Example 3:
        Input: matrix = [[1]]
        Output: [[1]]
        Example 4:
        Input: matrix = [[1,2],[3,4]]
        Output: [[3,1],[4,2]]

        Constraints:

        matrix.length == n
        matrix[i].length == n
        1 <= n <= 20
        -1000 <= matrix[i][j] <= 1000
                """

        for layer in range(len(matrix)//2):
            length = len(matrix) - layer*2
            for column in range(length-1):
                y1 = matrix[layer][column+layer]
                matrix[layer][column+layer] = matrix[length-1-column+layer][layer]
                matrix[length-1-column+layer][layer] = \
                    matrix[length - 1+layer][length-1-column+layer]
                matrix[length-1+layer][length-1-column + layer] = \
                    matrix[column+layer][length-1+layer]
                matrix[column+layer][length-1+layer] = y1
                # y2 = matrix[column+layer][length-1+layer]
                # y3 = matrix[length-1+layer][length-1-column+layer]
                # y4 = matrix[length-1-column+layer][layer]


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix)
assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution.rotate(matrix)
assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1],
                  [12, 6, 8, 9], [16, 7, 10, 11]]

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
solution.rotate(matrix)
assert matrix == [
    [21, 16, 11, 6, 1],
    [22, 17, 12, 7, 2],
    [23, 18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [25, 20, 15, 10, 5]
]


matrix = [[1]]
solution.rotate(matrix)
assert matrix == [[1]]

matrix = [[1, 2], [3, 4]]
solution.rotate(matrix)
assert matrix == [[3, 1], [4, 2]]
