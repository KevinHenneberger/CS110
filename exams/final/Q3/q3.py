try:
    user_input = int(input("Please enter a number: "))
except:
    print("I told you to enter a number!")
else:
    print("The square of your number is ", user_input ** 2)

try:
    user_input = int(input("Please enter a number: "))
except ValueError as e:
    print(e)
else:
    print("The square of your number is ", user_input ** 2)

print("The program did not break!")
