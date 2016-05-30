import sys
import character
import battle
import character
import town

def initialize_character(char_type, name):
    char = character.Character(char_type, name)
    return char

def town_menu(player):
    i = 0

if __name__ == "__main__":

    quit_game = False
    char_type = "player"
    player = character.Character("player")
    while not quit_game:
        print "Welcome to Arena Fighter v1.0"
        print
        print "Please select an option."
        print
        print "1) New Game"
        print "2) Load Game"
        print "3) Quit"
        choice = raw_input()
        if choice == 1:
            player.generate_new_character()
            # TODO: Add town menu
            player_group = [player]
            town_menu(player)
        if choice == 2:
            player.load_character()
            town_menu(player)
        if choice == 3:
            quit_game = True
        else:
            print "Invalid input."
            continue

        # Initialize Combat
        battle_group = [player, opponent]
        combat = battle.Battle(battle_group)

