def naive_solution_quadruplet(arr, s):
    final_list = list()
    for i in range(len(arr) - 3):  # 1
        for j in range(len(arr) - 2):  # 2
            for k in range(len(arr) - 1):  # 3
                for l in range(len(arr)):
                    if arr[i] + arr[j] + arr[k] + arr[l] == s:
                        final_list.append(arr[i])
                        final_list.append(arr[j])
                        final_list.append(arr[k])
                        final_list.append(arr[l])
                        final_list.sort(reverse=False)
                        return final_list
    return list()


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20


def find_array_quadruplet(arr, s):
    arr.sort()
    for i in range(len(arr) - 3):
        for j in range(i + 1, len(arr) - 2):
            # create two helper variables which are indexes of the first and last in the remaining elements
            l = j + 1
            r = len(arr) - 1

            # we need to find the remaining two elements, move the index variables closer together
            while l < r:
                if arr[i] + arr[j] + arr[l] + arr[r] == s:
                    final = [arr[i], arr[j], arr[l], arr[r]]
                    return sorted(final)
                elif arr[i] + arr[j] + arr[l] + arr[r] < s:
                    l += 1
                else:
                    r -= 1
    return list()


print(find_array_quadruplet(arr, s))

