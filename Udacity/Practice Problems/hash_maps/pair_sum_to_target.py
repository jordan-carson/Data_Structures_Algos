
def pair_sum_to_zero(input_list, target):

    index_dict = dict()
    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index


def pair_sum_to_zero(input_list, target):
    if len(input_list) <= 1:
        return False
    buff_dict = {}
    for i in range(len(input_list)):
        if input_list[i] in buff_dict:
            return [buff_dict[input_list[i]], i]
        else:
            buff_dict[target - input_list[i]] = i


if __name__ == '__main__':
    def test_function(test_case):
        output = pair_sum_to_zero(test_case[0], test_case[1])
        print(output)
        if sorted(output) == test_case[2]:
            print("Pass")
        else:
            print("Fail")


    test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
    test_function(test_case_1)

    test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
    test_function(test_case_2)

    test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
    test_function(test_case_3)