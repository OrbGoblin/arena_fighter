from random import randint
import uuid

# Contains all items and techniques
class Techniques():
    def __init__(self, target_type=""):
        self.id = uuid.uuid4().int
        self.target_type = target_type
        self.name = ""
        self.description = ""
        self.max_num_targets = 0
        # Techniques only
        self.ability_point_cost = 0
        # Items only
        self.money_cost = 0
        self.qty_on_hand


    def determine_list_of_targets(self, user, combat_group):
        return [target for target in combat_group if target.char_type == self.target_type]

    def activate_technique(self, user, list_of_targets):
        return None

    def choose_targets(self, list_of_targets):
        return None

class FireBall(Techniques):
    def __init__(self, target_type):
        Techniques.__init__(self, target_type)
        self.min_damage = 1
        self.max_damage = 10
        self.ability_point_cost = 3
        self.name = "Fireball"
        self.description = "Hits any number of opponents for " + str(self.min_damage) + " to " + str(self.max_damage) + " damage divided between them.\n" \
                          "Ability point cost: " + str(self.ability_point_cost)

    def activate_technique(self, user, list_of_targets):
        user.ability_points -= self.ability_point_cost
        print user.name + " shoots a fireball!"
        damage = randint(self.min_damage, self.max_damage)
        for target in list_of_targets:
            print target.name + " is hit with a fireball for " + damage + " damage!"
            target.health -= damage
            if target.health <= 0:
                print target.name + " is dead."
                target.is_dead = True

    def choose_targets(self, list_of_targets):
        return list_of_targets

class Heal(Techniques):
    def __init__(self, target_type):
        Techniques.__init__(self, target_type)
        self.total_heal = 5
        self.ability_point_cost = 2
        self.name = "Heal"
        self.description = "Heals any number of characters for " + str(self.total_heal) + " divided between them.\n" \
                                "Ability point cost: " + str(self.ability_point_cost)

    def activate_technique(self, user, list_of_targets):
        user.ability_points -= self.ability_point_cost
        print user.name + " uses heal!"
        for target in list_of_targets:
            print target.name + " is healed for " + str(self.total_heal / len(list_of_targets))
            if target.health + self.total_heal/len(list_of_targets) >= target.max_health:
                target.health = target.max_health
            target.health += self.total_heal / len(list_of_targets)

    def choose_targets(self, list_of_targets):
        chosen_targets = []
        done_choosing = False
        while not done_choosing:
            if len(chosen_targets) > 0:
                print "Targets currently chosen: "
                for target in chosen_targets:
                    print target.name

                print
            if len(list_of_targets) > 0:
                print "Unselected targets: "
                for target in list_of_targets:
                    print target.name
                print
            print "Would you like to add or remove a target?"
            print "Type done and press enter when finished."
            print
            choice = raw_input()
            if choice == "add" and len(chosen_targets) < len(list_of_targets):
                print "Choose a target to add:"
                for i in range(len(list_of_targets)-1):
                    target = list_of_targets[i]
                    print str(i+1) + ") " + target.name
                print
                choice = raw_input("")
                chosen_targets.append(list_of_targets[choice])
                del list_of_targets[choice]
            elif choice == "remove" and len(chosen_targets) > 0:
                print "Choose a target to remove:"
                for i in range(len(chosen_targets)-1):
                    target = list_of_targets[i]
                    print str(i+1) + ") " + target.name
                print
                choice = raw_input("")
                list_of_targets.append(chosen_targets[choice])
                del chosen_targets[choice]
            else:
                if choice != "done":
                    continue
                done_choosing = True

class Beep(Techniques):
    def __init__(self, target_type):
        Techniques.__init__(self, target_type)
        self.damage = 1
        self.ability_point_cost = 1
        self.name = "Beep"
        self.description =    "Damages all enemies for " + str(self.damage) + " damage.\n" \
                                   "Ability point cost: " + str(self.ability_point_cost)

    def activate_technique(self, user, list_of_targets):
        print user.name + " emits a shrieking beep!"
        for target in list_of_targets:
            print target.name + " takes " + str(self.damage) + " damage."
            target.health -= self.damage
            if target.health <= 0:
                print target.name + " has been killed!"
                target.is_dead = True

    def choose_targets(self, list_of_targets):
        return list_of_targets

class BeefJerky(Techniques):
    def __init__(self):
        Techniques.__init__(self, target_type="self")
        self.heal_amount = 3
        self.name = "Beef Jerky"
        self.description = "Heal yourself for " + str(self.heal_amount)
        self.money_cost = 20

    def determine_list_of_targets(self, user, combat_group):
            return [user]

    def choose_targets(self, list_of_targets):
        return list_of_targets

    def activate_technique(self, user, target):
        if self.heal_amount + target.health > target.max_health:
            self.heal_amount = target.max_health - target.health
        print "You eat some hearty " + self.name
        print "You are healed +" + self.heal_amount
        target.health += self.heal_amount