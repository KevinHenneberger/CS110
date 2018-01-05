import os 

path = "/Users/kevinhenneberger/documents/programming/os/test/dir-A1/dir-B2"

os.chdir(path)

files = os.listdir()

for f in files:
    os.rename(f, f.lower())
