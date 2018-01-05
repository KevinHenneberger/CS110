def main():

    fptr = open("original.txt", 'r')

    text = ""

    line = fptr.readline()

    while (line != ""):
        items = line.split()
        text += (items[1] + " " + items[0] + '\n')
        line = fptr.readline()

    fptr.close()

    fptr2 = open("new.txt", 'w')
    fptr2.write(text)
    fptr2.close()

main()
