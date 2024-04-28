class Tank:
    """representing game program name"""

    def __init__(
        self,
        cordinates_x: int = 3,
        cordinates_y: int = 10,
        direction: str = "^",
        shots_fired: int = 0,
        target_x: int = 0,
        target_y: int = 0,
    ):
        """representing methods"""
        self.cordinates_x = cordinates_x
        self.cordinates_y = cordinates_y
        self.target_x = target_x
        self.target_y = target_y
        self.shots_fired = shots_fired
        self.direction = direction

    def check_cordinate(self):
        """representing board of cordinates"""
        for x in range(5):
            for y in range(20):
                if x == self.cordinates_x and y == self.cordinates_y:
                    print(self.direction, end="")
                elif x == self.target_x and y == self.target_y:
                    print("0", end="")
                else:
                    print("_", end="")
            print()

    def move_forward(self):
        """representing tank move"""
        if self.direction == "^":
            self.cordinates_x -= 1
        elif self.direction == "v":
            self.cordinates_x += 1
        elif self.direction == "<":
            self.cordinates_y -= 1
        elif self.direction == ">":
            self.cordinates_y += 1
        else:
            print("wrong turn")

    def move_back(self):
        """representing tank move"""
        if self.direction == "^":
            self.cordinates_x += 1
        elif self.direction == "v":
            self.cordinates_x -= 1
        elif self.direction == "<":
            self.cordinates_y += 1
        elif self.direction == ">":
            self.cordinates_y -= 1
        else:
            print("wrong turn")

    def rotate_left(self):
        """representing rotation to left"""
        if self.direction == "^":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "^"
        return self.direction

    def rotate_rigth(self):
        """representing rotation to rigth"""
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == "<":
            self.direction = "^"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == ">":
            self.direction = "v"
        return self.direction

    # def shoot(self):
    #     """representing shots per direction"""
    #     self.shots_fired[self.direction] += 1

    def input_value(self):
        """representing direction values"""
        legal_input = [">", "<", "v", "^", "s", "i", "q"]
        text = """
        Galimos kryptys:
        > - East
        < - West
        v - South
        ^ - North
        s - shots
        i - info
        q:
        """
        value = input(text)
        if value not in legal_input:
            raise ValueError("tokia raide negalima")
        return value

    def rotate_tank(self, symbol):
        """representing tank rotation"""
        print("symbol:", symbol)

    def main(self):
        """representing checked values"""
        while True:
            try:
                value = self.input_value()
                print(value)
                if value == "q":
                    break
                elif value == "^":
                    self.rotate_tank(value)
                self.check_cordinate()
            except ValueError:
                print("neteisinga reiksme")


tank = Tank()
tank.main()
tank.check_cordinate()
