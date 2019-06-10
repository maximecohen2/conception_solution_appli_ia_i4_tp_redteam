import numpy as np
from enum import Enum
from environment import Action


class AI():
    def __init__(self, env, endeavours_bias=0.1, learning_rate=0.8):
        self.learning_rate = learning_rate
        self.endeavours_bias = endeavours_bias
        self.env = env
        num_states = env.COLS * env.ROWS
        num_actions = len(Action.all())
        self.qvalues = np.zeros((num_states, num_actions))

    def learn(self, steps):
        for _ in range(steps):
            self.env.reset()
            while not done:
                action = choose_action()
                reward, done = env.step(action)
                #td_target = reward + self.learning_rate * np.max(self.qvalues[self.get_state()])
                #self.qvalues[state][action] += td_target - qvalues[state][action]

    def choose_action(self):
        if np.random.random() < self.endeavours_bias:
            return np.random.choice(Action.all())
        else:
            return Action.all()[np.argmax(self.qvalues[self.get_state()])]

    def get_state(self):
        X, Y = 0, 1
        return self.env.position[X] + ( self.env.position[Y] * self.env.COLS )
