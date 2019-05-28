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
class Actions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Environment():
    def __init__(self, landform):
        self.landform = landform
        self._fill()
        self._build_reward_map()

    def get_max_row(self):
        return len(self.landform)

    def get_max_col(self):
        return max([len(row) for row in self.landform])

    def _build_reward_map(self):
        self.reward_map = []
        for row_index, row in enumerate(self.landform):
            self.reward_map.append([])
            for col_index, col in enumerate(row):
                self.reward_map[row_index].append(col.get_reward())

    def _fill(self):
        for row in self.landform:
            while len(row) < self.get_max_row():
                row.append(Map.DANGER)

    def step(self, action):
        if action == Actions.UP:
            if self.current_row != 0:
                current_row -= 1
        elif action == Actions.DOWN:
            if self.current_row != self.max_row:
                current_row += 1
        elif action == Actions.LEFT:
            if self.current_col != 0:
                current_col -= 1
        elif action == Actions.RIGHT:
            if self.current_col != self.max_col:
                current_col += 1
        state = current_col * current_row
        reward = reward_map[current_row][current_col]
        return (state, reward)

