def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a<b:
        testValue = a
    else:
        testValue = b
    while a%testValue != 0 or b%testValue !=0:
        testValue-=1
    return testValue
