class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.shots_fired = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    def forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1

    def back(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'W':
            self.x += 1

    def left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'S'

    def right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def shoot(self):
        self.shots_fired[self.direction] += 1

    def info(self):
        print('Direction:', self.direction)
        print('Coordinates:', (self.x, self.y))
        print('Total Shots Fired:', sum(self.shots_fired.values()))
        for direction, shots in self.shots_fired.items():
            print('Shots fired in', direction, 'direction:', shots)

tank = Tank()

while True:
    print("\n 1. forward, 2. back, 3. left, 4. right, 5. Shoot, 6. Info, 7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        tank.forward()
    elif choice == '2':
        tank.back()
    elif choice == '3':
        tank.left()
    elif choice == '4':
        tank.right()
    elif choice == '5':
        tank.shoot()
    elif choice == '6':
        tank.info()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")