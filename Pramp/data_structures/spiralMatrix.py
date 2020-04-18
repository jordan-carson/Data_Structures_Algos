# THIS IS BACKWARDS
def spiral_copy(inputMatrix):
    # k = len(inputMatrix) # row
    # l = len(inputMatrix[0]) # column
    # area = length(numberofrows) * width(numberofcols)
    # starting row index is 0
    row_index = 0
    # starting column index is 0
    col_index = 0
    number_of_rows = len(inputMatrix)  # length
    number_of_columns = len(inputMatrix[0])  # width
    start_row_position = 0
    start_column_position = 0
    direction = 0
    final_array = []
    #  for row in range(len(inputMatrix)):
    #    for col in range(len(inputMatrix[row])):
    for index in range(number_of_rows * number_of_columns):
        final_array.append(inputMatrix[row_index][col_index])  # 1 2 3 4 5

        # direction = (0-3)
        # is max col index and direction == 0
        #  direction += 1
        # is max row index and direction == 1
        #  direction += 1
        if col_index == number_of_columns - 1 and direction == 0:
            direction += 1
        elif row_index == number_of_rows - 1 and direction == 1:
            direction += 1
        elif col_index == start_column_position and direction == 2:
            direction += 1
            start_row_position = start_row_position + 1
        elif row_index == start_row_position and direction == 3:
            direction = 0
            number_of_rows = number_of_rows - 1
            number_of_columns = number_of_columns - 1
            start_column_position = start_column_position + 1

        if col_index < number_of_columns - 1 and direction == 0:  # 1 2 3 4 5 7 8 9
            # increment the number of columns

            col_index += 1

        # increment the number of rows
        # elif index >= number_of_columns and number_of_rows :
        elif row_index < number_of_rows - 1 and direction == 1:  # 10 15 20
            row_index += 1

        elif col_index > start_column_position and direction == 2:  # 19 18 17 16
            col_index -= 1

        elif row_index > start_row_position and direction == 3:  # 11 6
            row_index -= 1

        print(row_index, col_index)
        print(final_array)

    return final_array


# Test cases
print(spiral_copy([[1, 2], [4, 3]]))


class Iterator:
    def __init__(self, xlen, ylen):
        self.xlen, self.ylen = xlen, ylen
        self.x, self.y = 0, -1
        self.index, self.count = -1, xlen * ylen
        self.direction, self.gap = 0, 0
        self.__directionTable = {0: self.leftMax, 1: self.upMax, 2: self.rightMin, 3: self.downMin}

    def leftMax(self):
        return (self.y + 1 >= self.ylen - self.gap)  # approaching

    def upMax(self):
        return (self.x + 1 >= self.xlen - self.gap)  # approaching

    def rightMin(self):
        return (self.y <= self.gap)  # at

    def downMin(self):
        return (self.x <= self.gap)  # at

    def __direction(self):
        # when I change directions everything should be a MAX or MIN value
        if self.__directionTable[self.direction]():
            self.direction = (self.direction + 1) % 4
            if self.direction == 3: self.gap += 1

    def __increment(self):
        self.index += 1
        if self.direction == 0:
            self.y += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 3:
            self.x -= 1

    def next(self):
        if self.index + 1 >= self.count: return False
        self.__direction()
        self.__increment()
        return True

    def item(self):
        if self.index >= self.count: return None
        return (self.x, self.y)


def spiral_copy(inputMatrix, debug=True):
    global testResult
    if type(inputMatrix) != type([]) or not len(inputMatrix) or not len(inputMatrix[0]):
        return []

    iter = Iterator(len(inputMatrix), len(inputMatrix[0]))
    result = [None for x in range(iter.count)]
    while iter.next():
        x, y = iter.item()
        result[iter.index] = inputMatrix[x][y]

    if debug:
        for i in range(len(result)):
            if result[i] != testResult[i]:
                print("Values matched test, Failed!")

    return result


tests = [
    ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([[1, 2, 3], [6, 5, 4]], [1, 2, 3, 4, 5, 6]),
    (None, []),
    ([], []),
    ([[1]], [1]),
    ([[1, 2, 3]], [1, 2, 3]),
    ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
     [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12])
]

if __name__ == "__main__":
    for test in tests:
        testResult = test[1]
        print(spiral_copy(test[0], True))