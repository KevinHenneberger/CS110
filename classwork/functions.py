def multiply(num1, num2):

    product = 0

    for i in range(num2):
        product += num1

    return product

def power(num, pow):

    result = 1
    for i in range(pow):
        result *= num

    return result

def square(num):

    return multiply(num, num)

def main():

    print(multiply(3, 8))
    print(power(2, 8))
    print(square(10))

main()
