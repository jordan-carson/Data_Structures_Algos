def deletion_distance(str1, str2):
    memory = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        memory[i][0] = i

    for j in range(len(str2) + 1):
        memory[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                memory[i][j] = min(memory[i - 1][j - 1], memory[i - 1][j] + 1, memory[i][j - 1] + 1)
            else:
                memory[i][j] = min(memory[i - 1][j], memory[i][j - 1]) + 1

    return memory[len(str1)][len(str2)]  # your code goes here

