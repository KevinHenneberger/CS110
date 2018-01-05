import random

def generateCipher():

    sub_dict = {}

    # list of all possible substitution characters (ASCII 32-127)
    possible_sub_chars = [chr(c) for c in range(32, 127)]

    for k in range(32, 127):
        # choose a random substitution character from the list of random substitution characters
        rand_sub_char = random.choice(possible_sub_chars)
        # assign each key a random substitution character
        sub_dict[chr(k)] = rand_sub_char
        # remove the random substitution character from the list of possible random substitution characters so each key has a unique value
        possible_sub_chars.remove(rand_sub_char)
        
    return sub_dict

def encrypt(text, cipher):

    encrypted_text = ""

    for c in text:
        encrypted_text += cipher[c]

    return encrypted_text

def isValid(text):

    for c in text:
        if (not ord(c) in range(32, 127)):
            return False

    return True

def main():

    cipher = generateCipher()
    print("Cipher:")

    for key, val in cipher.items():
        print(key, val)

    print("=" * 50)

    # continuously prompt user for input
    while (True):

        text = input("Please enter some text to be encrypted (q to quit): ")

        while (not isValid(text)):
            text = input("Please enter some text to be encrypted: ")

        if (text == 'q'):
            print("Thank you for using this program!")
            break

        encrypted_message = encrypt(text, cipher)
        print(encrypted_message, end="\n\n")

main()
