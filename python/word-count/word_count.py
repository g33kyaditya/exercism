import string

def word_count(sentence):
    decoded = 'foo'
    try:
        decoded = sentence.decode('utf-8')
    except AttributeError:
        pass

    if decoded <> 'foo':
        sentence = decoded

    extras = list(string.punctuation + '\n\t')
    for char in extras:
        sentence = sentence.replace(char, ' ')
        sentence = sentence.replace(u'\U0001f596', ' ')

    words = sentence.lower().split(' ')
    dic = {}
    for word in words:
        if word <> '':
            dic[word] = dic.get(word, 0) + 1

    return dic
