

def sockMerchant(n, ar):
    aset = set()
    num_of_pairs = 0

    for i in ar:
        if i not in aset:
            aset.add(i)
        else:
            num_of_pairs += 1
            aset.remove(i)
    return num_of_pairs



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()