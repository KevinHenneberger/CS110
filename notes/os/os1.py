import os

path = "/Users/kevinhenneberger/documents/cs110/notes/"

for root, dirs, files in os.walk(path):
    print("=" * 75)
    print(root)
    print(dirs)
    print(files)
