def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    #filter(function, iterable)
    factors = [i for i in range(1,number) if number % i == 0 ]

    if sum(factors) == number:
        return "perfect"

    if sum(factors) < number:
        return "deficient"

    return "abundant"
