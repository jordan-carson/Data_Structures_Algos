import cProfile, random
def increment_string(strng):
    num = ''.join([i for i in strng if i.isdigit()])
    nonum = ''.join([i for i in strng if not i.isdigit()])
    if len(num) < 1:
        num = '1'
    return nonum + str(int(num) + 1)
    # return num

lIn = [random.random() for i in range(100000)]
cProfile.run('increment_string([1, 2, 3, 4, 5],9)')