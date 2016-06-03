import character

def save_game(player_group):
    for player in player_group:
        if player.char_type != "player":
            continue


def load_game(group_id):
    new_char = character.Character()