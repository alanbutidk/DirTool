import os

def osname():
    oswin = os.name
    if oswin == "nt":
        os.system("cls")
    elif oswin == "posix":
        os.system("clear")
    else:
        print(f"OS is {oswin}, Will add support next update :P")
print("Modes are: help, ., find, path, fulldir")
mode = input("Mode: ")
global findpath, findfile, path
if mode == "help":
    print("Python3 Os.listdir directory tool. Modes: help, ., find, path, fulldir")
    print("Made by alan :) Version 0.12")
    osname()
elif mode == ".":
    current = os.listdir(path=".")
    print(current)
    osname()
elif mode == "find":
    findpath = input("Path: ")
    findfile = input("file: ")
    if findfile in findpath:
        print("Found!")
    else:
        print("not found...")
    osname()
elif mode == "path":
    path = input("Path of directory: ")
    file = os.listdir(path)
    print(file)
    osname()
    
elif mode == "fulldir":
    fulldir = input("Enter the dir you want to fully scan: ")
    namerelated = input("The name you are trying to search: ")
    
    
    matches = set()  # set avoids duplicates automatically

    for root, dirs, files in os.walk(fulldir):
        for file in files:
            if namerelated.lower() in file.lower():
                full_path = os.path.join(root, file)
                matches.add(full_path)  # set ensures unique entries

    print("\n=== Scan Result ===")
    if matches:
        for m in sorted(matches):  # sorted for clean output
            print(m)
    else:
        print("No matching files found.")
    osname()