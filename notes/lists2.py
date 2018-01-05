def isPrime(n):

    for i in range(2, n):
        if (n % i == 0):
            return False

    return True

def primes(n):

    result = [i for i in range(2, n) if (isPrime(i))]
    return result

def main():

    kilometers = [20, 10, 5, 30]
    miles = []

    for i in kilometers:
        if (i * 0.621371 > 5):
            miles.append(i * 0.621371)

    print(miles)

    # list comprehension
    # expression, loop, *condition
    kilometers = [20, 10, 5, 30]
    miles = []

    miles = [i * 0.621371 for i in kilometers if (i * 0.621371 > 5)]

    print(miles)

    print(primes(25))

    # matrix and 2-dimensional list
    matrix = [list(range(5)) for i in range(5)]
    print(matrix)

    for row in range(5):
        for col in range(5):
            print(matrix[row][col], end=" ")

        print("")

main()
