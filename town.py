import sys
import character
import battle
import shop

class Town():
    def __init__(self):
        self.shop = shop.Shop()

    def main_menu(self, player_group):
        while True:
            print "Welcome to town, please select an option."
            print "1) Fight in the Arena"
            print "2) Item Shop"
            print "3) Visit Inn"
            print "4) Party Status"
            print "5) Save Game"
            print "6) Load Game"
            print "7) Quit Game"
            choice = int(raw_input())
            if choice == 1:
                opponent_group = self.generate_opponent_group()
                battle_group = player_group + opponent_group
                combat = battle.Battle(battle_group)
                combat.start_battle(battle_group)
            elif choice == 2:
                self.shop.main_menu(player_group)
            elif choice == 3:
                self.visit_inn(player_group)
            elif choice == 5:
                print "Feature not available"
            elif choice == 6:
                print "Feature not available"
            elif choice == 7:
                sys.exit(-1)

    def generate_opponent_group(self):
        opponent1 = character.Character("opponent")
        opponent2 = character.Character("opponent")
        return  [opponent1, opponent2]

    def visit_inn(self, player_group):
        sleep_cost = 15
        while True:
            print "Welcome to the Inn."
            print "Choose an option."
            print
            print "1) Rest"
            print "2) Listen for gossip."
            print "3) Leave"
            choice = int(raw_input())
            if choice == 1:
                # TODO: make sure you have enough money
                print "Your party rests."
                for player in player_group:
                    player.health = player.max_health
                    player.ability_points = player.max_ability_points
                    player.money -= sleep_cost
                    print player.name + " rests and is healed to full health."
            elif chocie == 2:
                print "Rumor has it this game is still in development..."
            elif choice == 3:
                break