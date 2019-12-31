def generate_hashtag(s):
    return False if (len(s) < 1 or len(s) > 140) else '#' + ''.join(word.capitalize() for word in s.strip().split(" ") if not word == "" or len(s) > 140)

def generate_hashtag_theirs(s):
    ans = '#' + str(s.title().replace(' ', ''))
    return s and not len(ans) > 140 and ans or False


print(generate_hashtag_theirs('         codewars  is  nice'))