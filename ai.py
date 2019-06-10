import numpy as np
from enum import Enum
from environment import Action


class AI():
    def __init__(self, env):
        self.random_endeavours_bias = 0.1
        self.env = env
        num_states = env.COLS * env.ROWS
        num_actions = len(Action.all())
        self.qvalues = np.zeros((num_states, num_actions))

    def learn(self, steps):
        for _ in range(steps):
            self.env.reset()
            while not done:
                action = choose_action()

    def choose_action(self):
        if np.random.random() < self.random_endeavours_bias:
            return np.random.choice(Action.all())
        else:
            return Action.all()[np.argmax(self.qvalues[self.get_state()])]

    def get_state(self):
        #return self.env.position[0]
        pass
