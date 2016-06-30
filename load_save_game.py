import os
import pickle
import character
from datetime import datetime

script_root = os.path.dirname(os.path.abspath(__file__))
save_load_root = os.path.join(script_root,"//saved_games//")
if not os.path.isdir(save_load_root):
    os.mkdir(save_load_root)

def save_game(player_group):
    for player in player_group:
        player.char_date = datetime.now().time()
        pickle_path = os.path.join(save_load_root, player.name)
        pickle.dump(player, open(pickle_path + ".p", mode="wb"))


def get_load_list():
    load_game_list = [os.path.join(save_load_root, game) for game in os.listdir(save_load_root) if game.endswith(".p")]
    player_list = []
    for game in load_game_list:
        tmp_char = pickle.load(open(game,mode="rb"))
        if tmp_char.char_type == "player":
            player_list.append(tmp_char)
    return player_list


def load_game():
    player_list = get_load_list()
    menu_choice = {}
    menu_idx = 1
    for player in player_list:
        menu_choice[menu_idx] = player
        print str(menu_idx) + ") " + player.name + " " + str(player.char_date)
        menu_idx += 1
    choice = int(raw_input())
    player_group = menu_choice[choice]
    return  player_group

