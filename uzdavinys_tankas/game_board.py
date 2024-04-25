for x in range(10):
    for y in range(10):
        if x == 2 and y == 2:
            print(">", end="")
        elif x == 5 and y == 5:
            print("0", end="")
        else:
            print("_", end="")
    print()
