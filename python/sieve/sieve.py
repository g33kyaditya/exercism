import math

def sieve(num):
    p = [True] * num
    p.append(True)
    ret = []
    for n in range(2, num + 1):
        if p[n] == True:
            ret.append(n)
            j = 2
            while j*n <= num:
                p[j*n] = False
                j += 1
    return ret
