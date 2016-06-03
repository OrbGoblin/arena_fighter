from random import randint
from techniques import Techniques


class Battle():
    def __init__(self, battle_group):
        #turned off for testing to stop infinite loop
        #self.start_battle(battle_group)
        self.battle_group = battle_group
        self.bonus_dodge = 0
        self.battle_over = False

    def start_battle(self, battle_group):
        print "Welcome to the battle!"
        player_list = []
        opponent_list = []
        for combatant in battle_group:
            if combatant.char_type == "player":
                player_list.append(combatant)
        for combatant in battle_group:
            if combatant.char_type == "opponent":
                opponent_list.append((combatant))
        print "Your group:"
        for player in player_list:
            print player.name
        print
        print "Opponents:"
        for opponent in opponent_list:
            print opponent.name
        print
        turn_counter = 0
        while not self.battle_over:
            turn_counter += 1
            print "Turn " + str(turn_counter)
            battle_order = self.determine_initiative(battle_group)
            for combatant in battle_order:
                retreat =  self.take_turn(combatant)
                if retreat:
                    self.battle_over = True
                if self.did_someone_win(battle_group, "player"):
                    self.battle_over = True
                if self.did_someone_win(battle_group, "opponent"):
                    self.battle_over = True

    def take_turn(self, combatant):
        if combatant.is_dead:
            return False
        if combatant.char_type == "opponent":
            choice = randint(1,100)
            if choice <= 50:
                list_of_opponents = [player for player in self.battle_group if player.char_type == "player" and player.is_dead == False]
                choice = randint(0,len(list_of_opponents)-1)
                opponent = list_of_opponents[choice]
                self.attack_opponent(combatant, opponent)
                return False
            else:
                list_of_opponents = [player for player in self.battle_group if
                                     player.char_type == "player" and player.is_dead == False]
                # TODO: replace this with something dynamic
                technique = combatant.technique_list[0]
                target = technique.determine_list_of_targets(combatant, list_of_opponents)
                technique.activate_technique(combatant, target)
                return False

        print "Choose an action: "
        print "1) Attack"
        print "2) Defend"
        print "3) Technique"
        print "4) Use Item"
        print "5) Retreat"
        choice = int(raw_input())
        # Attack
        if choice == 1:
            self.attack(combatant)

        # Defend
        if choice == 2:
            print "You defend."
            print
            if self.bonus_dodge <= 4:
                self.bonus_dodge += 1
                combatant.dodge += self.bonus_dodge
            else:
                print "You are at max bonus defense!"
                print

        # Technique & Item
        if choice == 3 or 4:
            if choice == 3:
                # TODO: put an error guard if they have no techniques
                self.run_technique_or_item(combatant, combatant.technique_list)
            elif choice == 4:
                # TODO: put an error guard if they have no items
                self.run_technique_or_item(combatant, combatant.inventory)

        # Retreat
        if choice == 5:
            chance_to_run = 50 + 5 * combatant.agility
            retreat_roll = randint(1,100)
            if retreat_roll >= chance_to_run:
                print "You retreat successfully"
                print
                self.battle_over = True
                return True
            print "The retreat failed!"
            print
        return False

    def run_technique_or_item(self, combatant, action_list):
        print "Please enter which technique or item you'd like to use."
        print "If you need info on what each technique or item does, enter help"
        print
        # TODO: Make sure have enough ability points and or inventory qty
        for i in xrange(len(action_list)):
            if isinstance(action_list, dict):
                action_list = [action for action in action_list]
            print str(i+1) + ") " + action_list[i].name
            choice = int(raw_input(""))
        if choice == "help":
            for action in action_list:
                print "Name: " + action.name
                print "Description: " + action.description
                print
        else:
            active_choice = action_list[choice-1]
            list_of_targets = active_choice.determine_list_of_targets(combatant, self.battle_group)
            chosen_targets = active_choice.choose_targets(list_of_targets)
            active_choice.activate_technique(combatant, chosen_targets)
            active_choice.cleanup(combatant)

    def attack(self, combatant):
        list_of_opponents = [opponent for opponent in self.battle_group if opponent.char_type == "opponent" and opponent.is_dead == False]
        print "Choose an opponent to attack!"
        for i in xrange(len(list_of_opponents)):
            print str(i+1) + ") " + list_of_opponents[i].name
        choice = int(raw_input())
        self.attack_opponent(combatant, list_of_opponents[choice-1])
        return choice


    def attack_opponent(self, combatant, opponent):
        print combatant.name + " attacks!"
        base_attack_chance = 50
        attack_delta = combatant.attack - opponent.dodge
        attack_chance = base_attack_chance + 5 * attack_delta
        attack_roll = randint(1, 100)
        if attack_roll <= attack_chance:
            print "Hit for " + str(combatant.damage) + "!"
            opponent.health -= (combatant.damage - opponent.armor)
            if opponent.health <= 0:
                print opponent.name + " is dead."
                print
                opponent.is_dead = True
        else:
            print "Miss!"
            print

    def did_someone_win(self, battle_group, char_type):
        char_type_dead_count = 0
        total_char_type = 0
        for combatant in battle_group:
            if combatant.char_type == char_type:
                total_char_type +=1
                if combatant.is_dead == True:
                    char_type_dead_count += 1
        if char_type_dead_count == total_char_type:
            print "The Battle has ended"
            print
            return True
        return False


    def determine_initiative(self, battle_group):
        ordered_battle_list = []
        for combatant in battle_group:
            combatant.initiative = randint(1, 6) * combatant.agility
            ordered_battle_list.append(combatant)
        ordered_battle_list.sort(key=lambda x: x.initiative, reverse=True)
        return ordered_battle_list