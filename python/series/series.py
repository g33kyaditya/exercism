def slices(foo, count):
    if count > len(foo) or count == 0:
        raise ValueError
    string = ''.join(foo)
    ret = []
    for i in range(0, len(string) - count + 1):
        k = i
        ct = 0
        current = []
        while ct != count:
            current.append(int(string[k]))
            k += 1
            ct += 1
        ret.append(current)
    return ret
