import random

def main():

    translate_dict = {
        "big": ["big league", "tremendous", "huge"],
        "good": ["fantastic", "the best"]
    } 

    otxtf = open("original.txt", "r")
    otxt = otxtf.read().split()
    otxtf.close()

    ntxt = ""

    for w in otxt:
        if (w in translate_dict):
            ntxt += random.choice(translate_dict[w])
        else:
            ntxt += w

        ntxt += ' '

    ntxtf = open("translated.txt", "w")
    ntxtf.write(ntxt)
    ntxtf.close()

main()
