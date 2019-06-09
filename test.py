import unittest
from environment import Environment, Map, Action


class TestMain(unittest.TestCase):
    def test_environnement_dimensions_computation(self):
        landform = [
            [Map.START, Map.LAND],
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
            [Map.START, Map.LAND],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND],
        ]
        expected = [
            [Map.START, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND, Map.DANGER],
        ]
        env = Environment(landform)
        self.assertEqual(expected, env.landform)

    def test_reward_map_building(self):
        landform = [
            [Map.START, Map.LAND, Map.DANGER],
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

    def test_starting_position_is_set(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.START, Map.DANGER],
        ]
        env = Environment(landform)
        self.assertEqual([1, 2], env.position)

    def test_steping_modify_the_position(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.START, Map.DANGER],
        ]
        env = Environment(landform)
        reward, done = env.step(Action.UP)
        self.assertEqual([1, 1], env.position)
        self.assertEqual(-1, reward)
        self.assertFalse(done)

    def test_steping_outside_of_bounds_is_like_danger_zone(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.START, Map.DANGER],
        ]
        env = Environment(landform)
        reward, done = env.step(Action.DOWN)
        self.assertEqual(Map.DANGER.get_reward(), reward)
        self.assertTrue(done)

    def test_steping_on_goal_land(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.START, Map.DANGER],
        ]
        env = Environment(landform)
        reward, done = env.step(Action.UP)
        reward, done = env.step(Action.RIGHT)
        self.assertEqual(Map.GOAL.get_reward(), reward)
        self.assertTrue(done)

    def test_landform_without_starting_point_creation(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.GOAL],
            [Map.DANGER, Map.LAND, Map.DANGER],
        ]
        with self.assertRaises(SystemExit):
            env = Environment(landform)

    def test_landform_without_goal(self):
        landform = [
            [Map.LAND, Map.LAND, Map.DANGER],
            [Map.DANGER, Map.LAND, Map.LAND],
            [Map.DANGER, Map.LAND, Map.DANGER],
        ]
        with self.assertRaises(SystemExit):
            env = Environment(landform)
