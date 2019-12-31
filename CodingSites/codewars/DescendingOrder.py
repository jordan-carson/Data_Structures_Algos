def descendingOrder(num):
    numstr = str(num)
    #     new_list = []
    #     for i in numstr:
    #         new_list.append(i)
    new_list = [i for i in numstr]
    new_list.sort()
    desc = new_list[::-1]
    return int(''.join(desc))

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


    # small_list = []
    # for i in num:


    # return


print(descendingOrder(1201))