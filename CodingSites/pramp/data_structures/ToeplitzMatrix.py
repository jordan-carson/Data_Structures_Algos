def isToeplitz(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr[0])-1):
      if arr[i][j] != arr[i+1][j+1]:
        return False
  return True


matrix = [[1,2,3,4],[5,1,2,3],[6,5,1,2]]

print(isToeplitz(matrix))
