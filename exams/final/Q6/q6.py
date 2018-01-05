import json

def main():

    fptr = open("data.json", "r")
    jsond = json.load(fptr)
    fptr.close()

    jsond["apple"] = 2.99
    jsond["watermelon"] = 3.49

    fptr = open("data.json", "w")
    fptr.write(json.dumps(jsond, indent=4))
    fptr.close()

main()
