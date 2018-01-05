#==============================
# CW Pt 1: Boolean Functions
#==============================
"""
def grade(score):

    if (score >= 90):
        return 'A'
    elif (score >= 80):
        return 'B'
    elif (score >= 70):
        return 'C'
    elif (score >= 60):
        return 'D'
    else:
        return 'F'

def isPassing(grade):
    if (grade == 'A' or grade == 'B' or grade == 'C'):
        return True
    else:
        return False

def main():

    score = int(input('Enter your score: '))
    letter_grade = grade(score)

    print(letter_grade)
    print(isPassing(letter_grade))

main()
"""

#==============================
# CW Pt 2: Boolean Functions
#==============================

def main():

    year = int(input('Enter a year: '))

    if (year >= 1900 and year < 3000):
        a = year % 19
        b = year // 100
        c = year % 100
        d = (((19 * a) + b) - (b // 4) - ((b - ((b + 8) // 25) + 1 ) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1

        print(str(month) + '/' + str(day) + '/' + str(year))
    else:
        print('Please enter a year between 1900 and 2099')

main()
