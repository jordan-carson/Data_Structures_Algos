
def spin_words(sentence):
    blank_str = ''
    for word in sentence.split():
        if not len(word) >= 5:
            blank_str = blank_str + ' ' + word
        else:
            blank_str = blank_str + ' ' + word[::-1]
    return blank_str.lstrip()
    # return ''.join(w[::-1] for w in sentence.split() if len(w) >= 5)


print(spin_words('Welcome my name is Jordan'))


def spin_words_theirs(sentence):
        # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])