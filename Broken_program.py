def fact(n):
    '''
    Реализация вычисления факториала.
    '''
    if n < 1:
        raise RecursionError
    if n == 1:
        return 1
    return n * fact(n - 1)


def result(a):
    b = fact(a)
    print(b)
    return b
