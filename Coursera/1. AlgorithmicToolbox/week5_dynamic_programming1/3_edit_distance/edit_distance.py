# Uses python3
def edit_distance(s, t):
    #write your code here
    mem = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    # print('Length of S is ' + str(len(s)))
    # print('Length of T is ' + str(len(t)))

    for i in range(0, len(s)+1):
        for j in range(0, len(t)+1):

            if i == 0:
                mem[i][j] = j

            elif j == 0:
                mem[i][j] = i

            elif s[i - 1] == t[j - 1]:
                mem[i][j] = mem[i - 1][j - 1]

            else:
                mem[i][j] = 1 + min(mem[i][j - 1],      # Insertion
                                    mem[i - 1][j],      # Deletion
                                    mem[i - 1][j - 1])  # Replace
    # pprint.pprint(mem)
    return mem[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
