import unittest
from environment import Environment, Map

class TestMain(unittest.TestCase):
    def test_environnement_dimensions_computation(self):
        landform = [
            [Map.LAND, Map.LAND],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND, Map.DANGER],
        ]
        env = Environment(landform)
        self.assertEqual(3, env.get_rows())
        self.assertEqual(3, env.get_cols())
        self.assertEqual(3, env.ROWS)
        self.assertEqual(3, env.COLS)

    def test_environnment_landform_filling(self):
        landform = [
            [Map.LAND, Map.LAND],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND],
        ]
        expected = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND, Map.DANGER],
        ]
        env = Environment(landform)
        self.assertEqual(expected, env.landform)

    def test_reward_map_building(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND, Map.DANGER],
        ]
        expected = [
            [-1, -1, -100],
            [-100, -1, 0],
            [-100, -1, -100]
        ]
        env = Environment(landform)
        self.assertEqual(expected, env.reward_map)
