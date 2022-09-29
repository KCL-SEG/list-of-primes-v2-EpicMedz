"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from logging import exception


def isNumPrime(number):
    if number == 2:
        return True
    else:
        for num in range(2, number):
            if (number % num) == 0:
                return False
        else:
            return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"Your value for {number_of_primes} should have been more than 0.")
    else:
        list = []
    count = 1
    numberToCheck = 2
    while count < number_of_primes + 1:
        if isNumPrime(numberToCheck):
            list.append(numberToCheck)
            count += 1
            numberToCheck += 1
        else:
            numberToCheck += 1
    print(f"{list}")
    return list
