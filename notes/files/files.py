"""
Files
- data permanence = saving to files
- read mode ('r')
- write mode ('w')
- append mode ('a')
"""

def main():

    fptr = open("text.txt", 'r')

    for line in fptr:
        print(line)

    #line = fptr.readline()
    #lines = fptr.readlines()
    #lines = fptr.read()
    fptr.close()

    fptr = open("text.txt", 'a')
    fptr.write("\nAdd this sample text.")

    fptr.close()

main()
