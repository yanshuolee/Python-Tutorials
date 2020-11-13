import pathlib

def multiplicationTable():
    i = 1
    j = 1
    while i <= 9:
        print(f"{i} x {j} = {i*j}")
        if 1 <= j < 9:
            j += 1
        else:
            j = 1
            i += 1
            print("==== 我是分隔線 ====")

def whereami():
    pwd = str(pathlib.Path("__file__").parent.absolute())
    print(f"Path: {pwd}")