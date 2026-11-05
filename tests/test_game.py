
import unittest

from game import new_game, apply_action

class TestNewGame(unittest.TestCase):

    def test_new_game_initial_state(self):
        player = new_game("Allen")

        self.assertEqual(player["name"], "Allen")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])
        self.assertFalse(player["searched_jungle"])

    def test_explore_moves_player_and_reduces_energy(self):
        player = new_game("Allen")

        apply_action(player, "explore")

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)  

    def test_cannot_enter_lighthouse_without_rope(self):
        player = new_game("Allen")

        player["location"] = "Old bridge"
        player["inventory"].append("lantern")

        message = apply_action(player, "explore")

        self.assertEqual(player["location"], "Old bridge")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(message, "You cannot proceed without a rope!")  
        
    def test_cannot_leave_cave_without_lantern(self):
        player = new_game("Allen")
        player["location"] = "Cave"

        message = apply_action(player, "explore")

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(
            message,
            "You must collect the lantern in the Cave first!"
        )

    def test_collect_rope_at_beach(self):
        player = new_game("Allen")

        message = apply_action(player, "collect_rope")

        self.assertIn("rope", player["inventory"])
        self.assertEqual(message, "You collected a rope!") 

    def test_collect_lantern_at_cave(self):
        player = new_game("Allen")
        player["location"] = "Cave"

        message = apply_action(player, "collect_lantern")

        self.assertIn("lantern", player["inventory"])
        self.assertEqual(player["energy"], 5)
        self.assertEqual(message, "You collected a lantern!")       
    
    def test_cannot_collect_rope_twice(self):
        player = new_game("Allen")

        apply_action(player, "collect_rope")
        message = apply_action(player, "collect_rope")

        self.assertEqual(player["inventory"].count("rope"), 1)
        self.assertEqual(message, "You already have a rope!")

    def test_search_jungle_reduces_energy(self):
        player = new_game("Allen")
        player["location"] = "Jungle"

        message = apply_action(player, "search_jungle")

        self.assertEqual(player["energy"], 3)
        self.assertTrue(player["searched_jungle"])
        self.assertIn("You found a clue!", message) 

    def test_searching_with_two_energy_causes_game_over(self):
        player = new_game("Allen")
        player["location"] = "Jungle"
        player["energy"] = 2

        apply_action(player, "search_jungle")

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])
        self.assertFalse(player["won"])    

    def test_restoring_beacon_wins_game(self):
        player = new_game("Allen")
        player["location"] = "Lighthouse"
        player["inventory"].append("lantern")

        message = apply_action(player, "restore_beacon")

        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])
        self.assertIn("Congratulations!", message)       

if __name__ == "__main__":
    unittest.main()
