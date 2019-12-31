# python3


def max_pairwise_product(numbers):
    # declare helpers
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(numbers)):

        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
            # print('i is', i, 'Numbers of i:', numbers[i], ': Largest is', largest, ': Second Largest', second_largest)
        elif numbers[i] > second_largest:
            second_largest = numbers[i]
            # print('i is', i, 'Numbers of i:', numbers[i], ': Largest is', largest, ': Second Largest', second_largest)

    return second_largest * largest

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))