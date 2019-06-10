from environment import Map, Environment
import os


class Shell():
    def __init__(self):
        self.landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND, Map.DANGER]
        ]
        self.env = Environment(self.landform)
        self.position = [0, 0]

    def display(self):
        self.display_landform()

    def display_landform(self):
        col_num = (self.env.get_max_col() * 2) - 1
        print("+{}+".format("-" * col_num))
        for y, row in enumerate(self.env.landform):
            to_display = "|"
            for x, land in enumerate(row):
                if self.position[0] == x and self.position[1] == y:
                    to_display += "X"
                elif land == Map.LAND:
                    to_display += " "
                elif land == Map.DANGER:
                    to_display += "+"
                elif land == Map.GOAL:
                    to_display += "O"
                if x+1 != len(row):
                    to_display += " "
            print(to_display + "|")
        print("+{}+".format("-" * col_num))
        print("reward: {}".format("0"))

    def mainloop(self):
        os.system("clear")
        self.display()
        input()
