def distance(one, another):
    if len(one) != len(another):
        raise ValueError('Error')

    count = 0
    for index in range(0, len(one)):
        if one[index] != another[index]:
            count += 1

    return count
