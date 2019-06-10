import unittest
from environment import Environment, Map, Action
from ai import AI

class TestAI(unittest.TestCase):
    def test_choose_action(self):
        env = Environment([[Map.START, Map.GOAL]])
        ai = AI(env)
        action = ai.choose_action()
        self.assertTrue(action in Action.all())

