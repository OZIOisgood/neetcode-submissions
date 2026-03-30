from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            temp = deque()

            for i in range(l, r):
                temp.append(matrix[t][i])
            for i in range(t, b):
                temp.append(matrix[i][r])
            for i in range(r, l, -1):
                temp.append(matrix[b][i])
            for i in range(b, t, -1):
                temp.append(matrix[i][l])

            # rotate clockwise
            temp.rotate(r - l)

            for i in range(l, r):
                matrix[t][i] = temp.popleft()
            for i in range(t, b):
                matrix[i][r] = temp.popleft()
            for i in range(r, l, -1):
                matrix[b][i] = temp.popleft()
            for i in range(b, t, -1):
                matrix[i][l] = temp.popleft()

            l += 1
            r -= 1
            t += 1
            b -= 1