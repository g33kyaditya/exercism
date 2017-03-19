def sum_of_multiples(number, array):
    s = 0
    for i in range(1, number):
        for z in array:
            if z !=0 and i%z == 0:
                s+= i
                break
    return s
