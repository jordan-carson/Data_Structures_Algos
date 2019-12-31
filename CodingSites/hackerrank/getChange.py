def get_change_greedy(m, den):

    if m == 0: return []
    for i in den:
        if i <= m:
            return [i] + get_change_greedy(m-i, den)
    # #write your code here
    # amount_of_ten = int(m / d[0])
    # amount_of_five = int((m - amount_of_ten * d[0]) / d[1])
    # amount_of_one = int(m - amount_of_ten * d[0] - amount_of_five * d[1])
    # return amount_of_ten + amount_of_five + amount_of_one


    # return m


print(get_change_greedy(24, [20, 8, 1]))