def is_palindrome(word): 
    reverse_word = word[::-1]
    return word == reverse_word

def main():
    print(is_palindrome('racecar'))
    print(is_palindrome('kevin'))

main()
