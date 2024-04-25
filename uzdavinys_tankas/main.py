class Tank:
    """representing game program name"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.shots_fired = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    def check_cordinates(self):
        """representing board of cordinates"""
        for x in range(10):
            for y in range(10):
                if x == self.x and y == self.y:
                    print("^", end="")
                # elif x == self.x and y == self.y:
                #     print("0", end="")
                else:
                    print("_", end="")
            print()

    def forward(self):
        """representing tank move"""
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1


tank = Tank()
tank.check_cordinates()
