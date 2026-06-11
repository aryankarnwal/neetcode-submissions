class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if target >= matrix[row][0] and target <= matrix[row][len(matrix[0])-1]:
                l = 0
                r = len(matrix[0]) - 1

                while l <= r:
                    m = (l+r)//2
                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
        return False