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

    def __hash__(self):
        return hash(self.name)

    def determine_list_of_targets(self, user, combat_group):
        return [target for target in combat_group if target.char_type == self.target_type]

    def activate_technique(self, user, list_of_targets):
        return None

    def choose_targets(self, list_of_targets):
        return None

    def cleanup(self, user):
        if self.type == "technique":
            user.ability_points -= self.ability_point_cost
            print user.name + " pays " + str(self.ability_point_cost) + " ability points."
        elif self.type == "item":
            print user.name + " uses up a " + self.name
            user.inventory[self] -= 1

class FireBall(Techniques):
    def __init__(self, target_type):
        Techniques.__init__(self, target_type)
        self.type = "technique"
        self.min_damage = 1
        self.max_damage = 10
        self.ability_point_cost = 3
        self.name = "Fireball"
        self.description = "Hits any number of opponents for " + str(self.min_damage) + " to " + str(self.max_damage) + " damage divided between them.\n" \
                          "Ability point cost: " + str(self.ability_point_cost)

    def activate_technique(self, user, list_of_targets):
        print user.name + " shoots a fireball!"
        damage = randint(self.min_damage, self.max_damage)
        for target in list_of_targets:
            print target.name + " is hit with a fireball for " + str(damage) + " damage!"
            target.health -= damage
            if target.health <= 0:
                print target.name + " is dead."
                target.is_dead = True
        print

    def choose_targets(self, list_of_targets):
        return list_of_targets

class Heal(Techniques):
    def __init__(self, target_type):
        Techniques.__init__(self, target_type)
        self.type = "technique"
        self.total_heal = 5
        self.ability_point_cost = 2
        self.name = "Heal"
        self.description = "Heals any number of characters for " + str(self.total_heal) + " divided between them.\n" \
                                "Ability point cost: " + str(self.ability_point_cost)

    def activate_technique(self, user, list_of_targets):
        if len(list_of_targets) <= 0:
            print "The tech has no target and fizzles"
            return
        print user.name + " uses heal!"
        for target in list_of_targets:
            print target.name + " is healed for " + str(self.total_heal / len(list_of_targets))
            if target.health + self.total_heal/len(list_of_targets) >= target.max_health:
                target.health = target.max_health
            target.health += self.total_heal / len(list_of_targets)

    def choose_targets(self, list_of_targets):
        selected_targets = []
        unselected_targets = []
        while True:
            if len(selected_targets) > 0:
                print "Targets currently chosen: "
                for target in selected_targets:
                    print target.name
                print
            if len(unselected_targets) > 0:
                print "Unselected targets: "
                for target in list_of_targets:
                    print target.name
                print
            print "Type add to select a target and remove to unselect?"
            print "Type done and press enter when finished."
            choice = raw_input()
            if choice == "add" and len(selected_targets) <= len(list_of_targets):
                print "Choose a target to add:"
                for i in range(len(list_of_targets)):
                    target = list_of_targets[i]
                    print str(i+1) + ") " + target.name
                print
                choice = int(raw_input("")) - 1
                choice = list_of_targets[choice]
                selected_targets.append(choice)
                # TODO: extract cleanup
                if len(unselected_targets) > 0:
                    for i in xrange(len(unselected_targets)):
                        if unselected_targets[i].name == choice.name:
                            del unselected_targets[i]

            elif choice == "remove" and len(selected_targets) > 0:
                print "Choose a target to remove:"
                for i in xrange(len(selected_targets)):
                    target = list_of_targets[i]
                    print str(i+1) + ") " + target.name
                choice = int(raw_input("")) - 1
                choice = selected_targets[choice]
                list_of_targets.append([choice])
                del selected_targets[choice]
            else:
                return selected_targets

class Beep(Techniques):
    def __init__(self, target_type):
        Techniques.__init__(self, target_type)
        self.type = "technique"
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
        self.type = "item"
        self.heal_amount = 3
        self.name = "Beef Jerky"
        self.description = "Heal yourself for " + str(self.heal_amount)
        self.money_cost = 20

    def determine_list_of_targets(self, user, combat_group):
            return user

    def choose_targets(self, list_of_targets):
        return list_of_targets

    def activate_technique(self, user, target):
        print "You eat some hearty " + self.name
        if self.heal_amount + target.health >= target.max_health:
            heal_text = str(target.max_health - target.health)
            target.health = target.max_health
            print "You healed " + heal_text
        else:
            target.health += self.heal_amount
            print "You are healed +" + str(self.heal_amount)

