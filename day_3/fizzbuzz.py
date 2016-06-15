def fizz_buzz(n):
    """ return fizz when n divisible by 3
    return buzz when n divisible by 5
    return fizzbuzz when n divisible by both 3 and 5
    """
    if n % 3 == 0:
        return 'fizz'
    else:
        return 'buzz'
