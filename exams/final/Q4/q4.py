try:
    fptr = open("mytextfile.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print(fptr.readline())

print("The program did not  break!")
