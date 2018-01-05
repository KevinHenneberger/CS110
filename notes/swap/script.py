import json

def main():

    fptr = open("data.json", "r")
    jsond = json.load(fptr)
    fptr.close()

    text = open("original.txt", "r").read()

    for key in jsond:
        text = text.replace(key, jsond[key])

    new = open("new.txt", "w")
    new.write(text)
    new.close()

main()
