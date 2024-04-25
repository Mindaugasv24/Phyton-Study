class Tank:
    def __init__(self, x=int, y=int, cordinates=int):
        self.x = x
        self.y = y
        self.cordinates = cordinates

    def check_cordinates(self):
        for x in range(10):
            for y in range(10):
                if x == self.cordinates_x and y == self.cordinates_y:
                    print(">", end="")
                elif x == self.cordinates_x and y == self.cordinates_y:
                    print("0", end="")
                else:
                    print("_", end="")
            print()
