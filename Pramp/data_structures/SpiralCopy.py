
def spiralCopy(inputMatrix):
    numRows = len(inputMatrix)
    numCols = len(inputMatrix[0])

    topRow = 0
    btmRow = numRows - 1
    leftCol = 0
    rightCol = numCols - 1

    result = []

    while topRow <= btmRow and leftCol <= rightCol:
        # copy the next top row
        for i in range(leftCol, rightCol+1):
            result.append(inputMatrix[topRow][i])
        topRow += 1

        # copy the next right hand side column
        for i in range(topRow, btmRow+1):
            result.append(inputMatrix[i][rightCol])
        rightCol -= 1

        # copy the next bottom row
        if topRow <= btmRow:
            for i in range(rightCol, leftCol+1):
                result.append(inputMatrix[btmRow][i])
            btmRow -= 1

        # copy the next left hand side column
        if leftCol <= rightCol:
            for i in range(btmRow, topRow+1):
                result.append(inputMatrix[i][leftCol])
            leftCol += 1

    return result

test_case = [
    [1, 2, 3, 4, 5],
    [6, 7, 6, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

print(spiralCopy(test_case))