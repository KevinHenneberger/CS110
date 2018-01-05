import stringoperations

def main():

    print("[" + ", ".join([chr(cc) for cc in range(97, 123)]) + "]")
    print(stringoperations.countCharacters("Banana"))
    print(stringoperations.countCharacters("I nip in; pin Pippin"))
    print(stringoperations.countCharacters("Blowzy night-frumps vex'd Jack Q"))

    stringLen = int(input("Enter desired string length: "))
    randomString = stringoperations.createRandomString(stringLen)
    print(randomString)
    print(stringoperations.countCharacters(randomString))

main()
