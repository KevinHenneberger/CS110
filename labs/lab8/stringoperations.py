import random

def createRandomString(num):
    """
    - Take an integer as a parameter and returns a random string containing <num> random characters.
    - a-z   => 97-122
    - A-Z   => 65-90
    - space => 32
    """

    randomCharacters = list(range(97, 123)) + list(range(65, 91)) + [32]
    randomString = ''

    for c in range(num):
        randomCharacter = random.choice(randomCharacters)
        randomString += chr(randomCharacter)

    return randomString

def countCharacters(countStr):
    """
    - Count the number of times each letter appears in a given string by taking an input string as a parameter and returning a list containing the counts. 
    - To do so we will need a list containing 26 integers all initialized to 0. 
    - Make sure your count is not case sensitive; in other words, count both upper and lower case.
    """

    countStr = countStr.lower()
    characterCount = [0] * 26

    for c in countStr:
        if (97 <= ord(c) <= 122):
            characterCount[ord(c) - 97] += 1

    return characterCount
    