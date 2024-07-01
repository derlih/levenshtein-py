from typing import List


class Matrix:
    _data: List[List[int]]

    def __init__(self, width: int, height: int) -> None:
        self._data = [[0 for _ in range(height)] for _ in range(width)]
        for i in range(width):
            self._data[i][0] = i

        for i in range(height):
            self._data[0][i] = i

    def get_item(self, x: int, y: int) -> int:
        return self._data[x][y]

    def set_item(self, x: int, y: int, v: int) -> None:
        self._data[x][y] = v


def full_matrix(a: str, b: str) -> int:
    len_a = len(a)
    len_b = len(b)
    matrix = Matrix(len_a + 1, len_b + 1)

    for j in range(1, len_b + 1):
        for i in range(1, len_a + 1):
            if a[i - 1] == b[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            matrix.set_item(
                i,
                j,
                min(
                    matrix.get_item(i - 1, j) + 1,
                    matrix.get_item(i, j - 1) + 1,
                    matrix.get_item(i - 1, j - 1) + substitution_cost,
                ),
            )

    return matrix.get_item(len_a, len_b)
