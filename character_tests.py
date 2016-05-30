import unittest
import character



class CharacterTests(unittest.TestCase):
    def character_stats_check(self, test_char, char_type, char_name):
        self.assertEqual(char_type, test_char.char_type)
        self.assertEqual(char_name, test_char.name)

    def test_init(self):
        num_of_chars = 10
        for char in range(num_of_chars):
            if char == 1:
                char_name = "Test Name"
                char_type = "player"
                test_char = character.Character(char_type, char_name)
                self.character_stats_check(test_char, char_type, char_name)
            if char == 2:
                char_name = "Test Name"
                char_type = "opponent"
                test_char = character.Character(char_type, char_name)
                self.character_stats_check(test_char, char_type, char_name)
            else:
                char_name = "Test"
                char_type = "Test"
                test_char = character.Character(char_type, char_name)
                self.character_stats_check(test_char, char_type, char_name)

if __name__ == "__main__":
    unittest.main()