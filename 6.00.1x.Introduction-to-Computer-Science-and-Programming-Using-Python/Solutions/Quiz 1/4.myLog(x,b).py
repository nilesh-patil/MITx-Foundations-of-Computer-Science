def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x <= 0 or b <= 0:
        raise Exception("Invalid input!")
    
    if b == 1:
        return float("+inf")
    
    result = b
    n = 0
    while result <= x:
        result*=b
        n+=1
    return n