# Binary Numbers


num = int(input())

count, minimum = 0, 0

while num > 0:

    if num % 2 == 1:
        count += 1
        if count > minimum:
            minimum = count
    else:
        count = 0

    num //= 2

print(minimum)




# print(binary)