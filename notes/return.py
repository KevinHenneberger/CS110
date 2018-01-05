def isDivisible(x, y):
    # if (x % y == 0):
    #     return True
    # else:
    #     return False

    return x % y == 0

def main():
    print(isDivisible(10, 5))

    if (isDivisible(10, 5)):
        print("x is divisible by y")

main()
