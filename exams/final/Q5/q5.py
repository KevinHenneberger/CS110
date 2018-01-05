import random

def main():

    my_list = [12, 3, 123, 12, 3, 123, 1, 2, "a", "sfasfas"]
    random_element = random.choice(my_list)
    
    try:
        print(random_element ** 2)
    except TypeError as e:
        print(e)
        print("You can't square a string!")    

main()
