def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print("{}".format(index))

#https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
#https://repl.it/repls/SatisfiedKnownTwintext
#http://pythontesting.net/framework/unittest/unittest-introduction/
