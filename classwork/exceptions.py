def foo(string):

    try:
        for c in string:
            print(c)
    except:
        print(string)
                

def main():

    foo("dog")
    foo(123)

main()
