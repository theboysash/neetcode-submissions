class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        firstVals = []
        for i in range(0, m):
            firstVals.append(matrix[i][0])

        low = 0
        high = len(firstVals) - 1
        column = -1

        while low <= high:
            mid = (low + high) // 2
            if target == firstVals[mid]:
                column = mid
                break
            if target < firstVals[mid]:
                high = mid - 1
            else:
                low = mid + 1

        if column == -1:
            column = high  # last row whose first value is <= target

        if column < 0:
            return False  # target is smaller than every row's first value

        n = len(matrix[column])
        low2 = 0
        high2 = n - 1
        while low2 <= high2:
            mid2 = (low2 + high2) // 2
            if matrix[column][mid2] == target:
                return True
            elif target < matrix[column][mid2]:
                high2 = mid2 - 1
            else:
                low2 = mid2 + 1

        return False