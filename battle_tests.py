import unittest
import mock
import character
import battle

class BattleTests(unittest.TestCase):

    def setUp(self):
        self.battle_group = self.generate_battle_group()
        self.combat = battle.Battle(self.battle_group)

    def generate_battle_group(self):
        char1 = character.Character("player")
        char2 = character.Character("player")
        char3 = character.Character("player")
        opponent1 = character.Character("opponent")
        opponent2 = character.Character("opponent")
        opponent3 = character.Character("opponent")
        battle_group = [char1, char2, char3, opponent1, opponent2, opponent3]
        return battle_group

    def test_determine_initiative(self):
        battle_size = len(self.battle_group)
        agility_list = [1, -43, -7, 43, -1, 7]
        for i in xrange(battle_size):
            self.battle_group[i].agility = agility_list[i]
        expected = [self.battle_group[3], self.battle_group[5], self.battle_group[0], self.battle_group[4], self.battle_group[2], self.battle_group[1]]
        actual = self.combat.determine_initiative(self.battle_group)
        for result in range(len(expected)):
            self.assertEqual(expected[i].agility, actual[i].agility)

    def test_did_someone_win(self):
        char_type = "player"
        self.assertFalse(self.combat.did_someone_win(self.battle_group, char_type))
        char_type = "opponent"
        self.assertFalse(self.combat.did_someone_win(self.battle_group, char_type))
        for combatant in self.battle_group:
            if combatant.char_type == char_type:
                combatant.is_dead = True
            else:
                combatant.is_dead = False
        self.assertTrue(self.combat.did_someone_win(self.battle_group, char_type))
        char_type = "player"
        for combatant in self.battle_group:
            if combatant.char_type == char_type:
                combatant.is_dead = True
            else:
                combatant.is_dead = False
        self.assertTrue(self.combat.did_someone_win(self.battle_group, char_type))
        for combatant in self.battle_group:
            if combatant.char_type == char_type:
                combatant.is_dead = False
                break
        self.assertFalse(self.combat.did_someone_win(self.battle_group, char_type))

    def test_take_turn(self):
        combatant = self.battle_group[0]
        combatant.char_type = "opponent"
        self.assertFalse(self.combat.take_turn(combatant))
        combatant.is_dead = True
        self.assertFalse(self.combat.take_turn(combatant))

    def test_attack(self):
        battle_group = self.generate_battle_group()



if __name__ == "__main__":
    unittest.main()