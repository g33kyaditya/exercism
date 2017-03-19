import string

def is_pangram(sentence) :
    dict = {}
    alphabets = set(string.ascii_lowercase)
    sentence = sentence.lower()
    for alphabet in alphabets :
        if alphabet not in sentence :
            return False

    return True