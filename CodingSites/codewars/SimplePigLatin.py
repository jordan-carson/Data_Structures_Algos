def pig_it(text):
    l = []
    for word in text.split(' '):
        if word in '!@#$%^&*()?><':
            l.append(word)
        else:

            l.append(word[1:] + word[0] + 'ay')
    return ' '.join(i for i in l)


def pig_it2(text):
    return ' '.join(x[1:] + x[0] + 'ay'if x.isalpha() else x for x in text.split(' '))


def pig_it_theirs(text):
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split()])


assert pig_it2('O tempora o mores !') == 'Oay emporatay oay oresmay !'

