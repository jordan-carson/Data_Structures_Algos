N = int(input())

phone_book= {}

for i in range(0, N):

    entry = str(input()).split(" ")
    # print(entry[0], entry[1])
    name = entry[0]
    phonenumber = int(entry[1])
    phone_book[name] = phonenumber

    # print(phone_book)

for j in range(0, N):

    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name, "=", str(phone), sep="")
    else:
        print('Not found')