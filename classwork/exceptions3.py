import math

def main():

    try:
        num = int(input("Please enter a number: "))
        better_num = 5 / num
        print(better_num)
    except ValueError as err:
        print(err)
    except ZeroDivisionError as err:
        print(err)
    except Exception as err:
        print(err)

main()
