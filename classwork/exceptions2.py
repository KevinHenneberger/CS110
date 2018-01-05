class WrongAnswerError(Exception):
    pass

class NoAnswerError(Exception):
    pass

def isValid1(food):
    if (food == ""):
        raise NoAnswerError

def isValid2(food):
    if (food != "pizza"):
        raise WrongAnswerError

def main():

    food = input("Enter your favorite food: ")

    try:
        isValid1(food)
        isValid2(food)
    except WrongAnswerError as err:
        print("WrongAnswerError")
    except NoAnswerError as err:
        print("NoAnswerError")

main()
