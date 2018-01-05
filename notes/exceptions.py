def main():

    try:
        fptr = open("dne.txt", "r")
    except FileNotFoundError as e: 
        print(e)

main()
