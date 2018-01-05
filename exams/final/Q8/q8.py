class MyException(Exception):
    def __str__(self):
        return "My Exception!"

def isValid(val):

    if (val % 2 == 0):
        raise MyException

def main():

    try:
        isValid(4)
    except MyException as e:
        print(e)

main()
