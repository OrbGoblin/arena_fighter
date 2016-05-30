import sys
import character
import battle
import shop

class Town():

    def main_menu(self, player_group):
        print "Welcome to town, please select an option."
        print "1) Fight in the Arena"
        print "2) Item Shop"
        print "3) Party Status"
        print "4) Save Game"
        print "5) Load Game"
        print "6) Quit Game"
        choice = raw_input()
        if choice == 1:
            opponent_group = self.generate_opponent_group()
            battle_group = player_group + opponent_group
            combat = battle.Battle(battle_group)
            combat.start_battle(battle_group)
        elif choice == 2:
            shop.main_menu(player_group)
        elif choice == 3:
            print "Feature not available"
        elif choice == 4:
            print "Feature not available"
        elif choice == 5:
            print "Feature not available"
        elif choice == 6:
            sys.exit(-1)

    def generate_opponent_group(self):
        opponent1 = character.Character("opponent")
        opponent2 = character.Character("opponent")
        return  [opponent1, opponent2]