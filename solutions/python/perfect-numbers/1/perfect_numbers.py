def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors = []
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for nums in range(1, number):
        if number == nums:
            continue
        if number % nums == 0:
            factors.append(nums)
    if sum(factors) > number:
        return "abundant"
    if sum(factors) < number:
        return "deficient"
    return "perfect"