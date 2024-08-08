import matplotlib.pyplot as plt
import random


class Room:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]
        self.total_tiles = width * height
        self.cleaned_tiles = 0

    def clean(self, x, y):

        if self.tiles[y][x] == 0:
            self.tiles[y][x] = 1
            self.cleaned_tiles += 1

    def cleaned_precentage(self):

        return (self.cleaned_tiles / self.total_tiles) * 100


class Robot:

    def __init__(self, room):

        self.room = room

        self.x = random.randint(0, room.width - 1)

        self.y = random.randint(0, room.height - 1)

        print(f"Robot initialized at : {self.x} , {self.y}")

    def move_clean(self):

        self.room.clean(self.x, self.y)

        self.x = random.randint(0, self.room.width - 1)

        self.y = random.randint(0, self.room.height - 1)

        print(f"Robot has moved to {self.x} , {self.y}")


def main():

    while True:
        try:
            width = int(input("Enter width for the room : "))
            if width <= 0:
                raise ValueError
            break

        except ValueError:
            print(" Invalid input , Enter a postive number for the width.")

    while True:
        try:
            height = int(input("Enter height for the room : "))
            if height <= 0:
                raise ValueError
            break

        except ValueError:
            print(" Invalid input , Enter a postive number for the height.")

    while True:
        try:
            number_robots = int(input("Enter how many robots to clean the room : "))
            if number_robots <= 0:
                raise ValueError
            break

        except ValueError:
            print(" Invalid input , Enter a postive number for the robots.")

    while True:
        choice = (
            input(
                "Choose 'time' to see time that takes to clean a room targeting a percentage or choose 'percentage' to see the percentage cleaned in a given time: "
            )
            .strip()
            .lower()
        )
        if choice not in ["time", "percentage"]:
            print("Invalid input. Enter 'time' or 'percentage'.")
            continue
        if choice == "time":
            while True:
                try:
                    target = float(input("Enter the target percentage to be cleaned: "))
                    if not 0 <= target <= 100:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Enter a percentage between 0 and 100.")
            break
        elif choice == "percentage":
            while True:
                try:
                    target = float(input("Enter the time in seconds: "))
                    if target <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Enter a positive number for the time.")
            break

    room = Room(width, height)
    robots = [Robot(room) for _ in range(number_robots)]

    fig, ax = plt.subplots()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_xticks(range(width + 1))
    ax.set_yticks(range(height + 1))
    ax.grid()



    for frame in range(1000):
        for robot in robots:
            robot.move_clean()
        cleaned_percentage_room = room.cleaned_precentage()
        ax.clear()
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_xticks(range(width + 1))
        ax.set_yticks(range(height + 1))
        ax.grid()
        for y in range(room.height):
            for x in range(room.width):
                if room.tiles[y][x] == 1:
                    particularBox_xCoord = [x, x, x + 1, x + 1, x]
                    particularBox_yCoord = [y, y + 1, y + 1, y, y]
                    ax.plot(particularBox_xCoord, particularBox_yCoord, "blue")
        ax.set_title(f"Cleaned: {cleaned_percentage_room:.2f}%")

        print(f"Frame: {frame}, Cleaned Percentage: {cleaned_percentage_room:.2f}%")

        if choice == "time" and cleaned_percentage_room >= target:
            print(f"Time to clean {target}%: {frame / 10.0:.1f} seconds")
            break
        elif choice == "percentage" and frame / 10.0 >= target:
            print(
                f"Percentage cleaned in {target} seconds: {cleaned_percentage_room:.2f}%"
            )
            break

        plt.pause(0.1)

    plt.show()


main()
