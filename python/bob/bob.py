#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    what = ' '.join(what.split())
    if what == '':
        return 'Fine. Be that way!'
    elif what[-1] == '?' and not what.isupper():
        return 'Sure.'
    elif what.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

