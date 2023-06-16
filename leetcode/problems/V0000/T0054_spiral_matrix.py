""" 0054. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
  * m == matrix.length
  * n == matrix[i].length
  * 1 <= m, n <= 10
  * -100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    """ Spiral Matrix """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ Решение задачи """

        result = []
        if not matrix:
            return result

        rows, columns = len(matrix), len(matrix[0])
        row, column = 0, -1

        while True:

            # Перемещаемся слева направо
            for _ in range(columns):
                column += 1
                result.append(matrix[row][column])

            rows -= 1
            if rows <= 0: break

            # Перемещаемся сверху вниз
            for _ in range(rows):
                row += 1
                result.append(matrix[row][column])

            columns -= 1
            if columns <= 0: break

            # Перемещаемся справа налево
            for _ in range(columns):
                column -= 1
                result.append(matrix[row][column])

            rows -= 1
            if rows <= 0: break

            # Перемещаемся снизу вверх
            for _ in range(rows):
                row -= 1
                result.append(matrix[row][column])

            columns -= 1
            if columns <= 0: break

        return result
