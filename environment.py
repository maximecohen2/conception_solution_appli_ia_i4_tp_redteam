from enum import Enum, unique


@unique
class Map(Enum):
    LAND = 0
    START = 1
    GOAL = 2
    DANGER = 3

    def get_reward(self):
        if self == self.LAND:
            return -1
        elif self == self.START:
            return -1
        elif self == self.GOAL:
            return 0
        elif self == self.DANGER:
            return -100


@unique
class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Environment():
    def __init__(self, landform):
        self.position = None
        self.goal_position = None
        self.reward_map = []
        self.landform = landform
        for row_index, row in enumerate(self.landform):
            self.reward_map.append([])
            while len(row) < self.get_rows():
                row.append(Map.DANGER)
            for col_index, col in enumerate(row):
                self.reward_map[row_index].append(col.get_reward())
                if col == Map.START:
                    self.position = [col_index, row_index]
                elif col == Map.GOAL:
                    self.goal_position = [col_index, row_index]
        if self.position == None:
            exit("Starting land not found in landmap.")
        self.ROWS = self.get_rows()
        self.COLS = self.get_cols()

    def get_rows(self):
        return len(self.landform)

    def get_cols(self):
        return max([len(row) for row in self.landform])

    def step(self, action):
        X, Y = 0, 1
        if action == Action.UP:
            if self.position[Y] != 0:
                self.position[Y] -= 1
        elif action == Action.DOWN:
            if self.position[Y] != self.ROWS:
                self.position[Y] += 1
        elif action == Action.LEFT:
            if self.position[X] != 0:
                self.position[X] -= 1
        elif action == Action.RIGHT:
            if self.position[X] != self.COLS:
                self.position[X] += 1
        done = False
        try:
            reward = self.reward_map[self.position[Y]][self.position[X]]
            done = True if self.position == self.goal_position else False
        except IndexError:
            reward = Map.DANGER.get_reward()
            done = True
        return (reward, done)
