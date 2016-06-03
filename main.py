import uuid
import battle
import character
import town
import load_save_game

if __name__ == "__main__":

    quit_game = False
    char_type = "player"
    char_name = "Test McTesterton"
    player = character.Character(char_type, char_name)
    active_town = town.Town()
    while not quit_game:
        print "Welcome to Arena Fighter v1.0"
        print
        print "Please select an option."
        print
        print "1) New Game"
        print "2) Load Game"
        print "3) Quit"
        choice = int(raw_input())
        if choice == 1:
            player.generate_new_character()
            player_group = [player]
            quit_game = active_town.main_menu(player_group)
        if choice == 2:
            player.load_character()
            quit_game = active_town.main_menu(player)
        if choice == 3:
            quit_game = True
        else:
            print "Invalid input."
            continue


