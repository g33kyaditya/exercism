def square_of_sum(num):
    ssum = (num*(num + 1))/2
    return ssum**2

def sum_of_squares(n):
    ssum = ( n*(n+1)*(2*n + 1) )/6
    return ssum

def difference(num):
    return square_of_sum(num) - sum_of_squares(num)
