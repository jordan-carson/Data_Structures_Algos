actual = str(input()).split(" ")


expect = str(input()).split(" ")


def fine(actual, expect):
    da, ma, ya = int(actual[0]), int(actual[1]), int(actual[2])
    de, me, ye = int(expect[0]), int(expect[1]), int(expect[2])
    fine = 0
    if ya > ye:
        fine = 10000
    elif ya == ye:
        if ma > me:
            fine =  500 * (int(ma) - int(me))
        elif ma == me and da > de:
            fine = 15 * (int(da) - int(de))
    return fine



print(fine(actual, expect))
