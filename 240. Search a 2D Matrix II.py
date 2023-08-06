def searchMatrix(matrix, target):
    for row in matrix:
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return False

matrix = [[1, 4], [2, 5]]
target = 2
result = searchMatrix(matrix, target)
print(result)  # This will print "True"
