import random

"""
# CW - Pt 1
1) True
2) False
3) False
4) True
5) True
6) True
7) False
8) True
9) False
10) False
11) True
12) False
13) True
14) False
15) False
16) False
17) True
18) True
19) False
20) False
"""

# CW - Pt 3
def numberGuess():

    random_number = random.randint(1, 10) 

    for g in range(3):

        guess = int(input('Guess the number: '))

        if (guess == random_number):
            print('Correct!')
            break
        elif (guess < random_number):
            print('Too Low')
        elif (guess > random_number):
            print('Too High')

def main():

    """
    # CW - Pt 2
    num = int(input('Please enter a number: '))

    if (num < 0):
        print(num + abs(num))
    else:
        print(num + -(num))
    """

    numberGuess()

main()
