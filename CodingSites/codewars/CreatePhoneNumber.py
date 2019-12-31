def create_phone_number(n):
    nstr = ''.join(str(x) for x in n)
    # print(to3)
    return '({}) {}-{}'.format(nstr[:3],nstr[3:6],nstr[6:10])
    #your code here

def create_phone_number_theirs(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1,2,3,4,5,6,7,8,9,10]))
print(create_phone_number_theirs([1,2,3,4,5,6,7,8,9,1]))



