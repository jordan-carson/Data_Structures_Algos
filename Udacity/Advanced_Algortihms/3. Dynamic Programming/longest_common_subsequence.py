# The time complexity of the above implementation
# is dominated by the two nested loops,
# which give us an O(N^2) time complexity.


def lcs_mine(string_a, string_b):
    mem = [[0 for _ in range(len(string_b)+1)] for _ in range(len(string_a)+1)]
    for i in range(len(string_a)+1):
        for j in range(len(string_b)+1):
            if i == 0 or j == 0:
                mem[i][j] = 0
            elif string_a[i-1] == string_b[j-1]:
                mem[i][j] = mem[i-1][j-1] + 1
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])
    return mem[len(string_a)][len(string_b)]


def lcs_udacity(string_a, string_b):
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    for char_a_i, char_a in enumerate(string_a):
        for char_b_i, char_b in enumerate(string_b):
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    return lookup_table[-1][-1]


# The time complexity of the above implementation
# is dominated by the two nested loops,
# which give us an O(N^2) time complexity.

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs_mine(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs_mine(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)

assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)

assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')