def encode(string):
    ret = ''
    count = 1
    i = 0
    while i < len(string):
        count = 1
        for j in range(i+1, len(string)):
            if string[j] == ' ' or string[j] <> string[i]:
                break
            count += 1
        if count > 1:
            ret += str(count) + string[i]
        else:
            ret += string[i]
        i += count

    return ret

def decode(string):
    ret = ''
    times = 0
    for i in range(0, len(string)):
        if string[i].isdigit():
            times = 10*times + int(string[i])
        else:
            current = string[i]
            if times == 0:
                times = 1
            for k in range(0, times):
                ret += current
            times = 0
    return ret

'''if __name__ == '__main__':
    print encode('AABBBCCCC')
    print decode(encode('AABBBCCCC'))
    print decode('2A3B4C')
'''
