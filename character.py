import uuid
import techniques

class Character():
    def __init__(self, char_type="", name=""):
        self.char_type = char_type
        self.name = name
        self.id = uuid.uuid4().int
        # not preserved save/load
        self.list_of_professions = ["fighter", "engineer", "rogue"]
        self.list_of_races = ["Human", "Mutant", "Cyborg"]

        self.skill_points = 0
        # TODO: figure out a way to have money consolidate for a group
        self.money = 100
        # opponent only
        if char_type == "player":
            self.group_id = uuid.uuid4().int
        if char_type == "opponent":
            self.set_opponent()
        # player only




    # Set hash value so we can store characters in dictionaries
    def __hash__(self):
        return self.id

    def set_player_stats(self):
        if self.profession == "fighter":
            self.attack = 7
            self.dodge = 1
            self.damage = 6
            self.armor = 1
            self.max_health = 30
            self.health = self.max_health
            self.max_ability_points = 5
            self.ability_points = self.max_ability_points
            self.agility = 1
            self.is_dead = False
            self.technique_list = []
            # Key is inventory object, val is qty
            self.inventory = {techniques.BeefJerky(): 5}
        if self.profession == "engineer":
            self.attack = 3
            self.dodge = 1
            self.damage = 2
            self.armor = 0
            self.max_health = 20
            self.health = self.max_health
            self.max_ability_points = 15
            self.ability_points = self.max_ability_points
            self.agility = 1
            self.is_dead = False
            self.technique_list = [techniques.FireBall("opponent"), techniques.Heal("player")]
            # Key is inventory object, val is qty
            self.inventory = {techniques.BeefJerky(): 5}
        if self.profession == "rogue":
            self.attack = 7
            self.dodge = 2
            self.damage = 5
            self.armor =0
            self.max_health = 20
            self.health = self.max_health
            self.max_ability_points = 10
            self.ability_points = self.max_ability_points
            self.agility = 2
            self.is_dead = False
            self.technique_list = []
            # Key is inventory object, val is qty
            # TODO: change this to a list, put inventory as an attribute in techniques.py
            self.inventory = {techniques.BeefJerky(): 5}

    def adjust_race_stats(self):
        if self.race == "Human":
            self.max_ability_points += 5
            self.ability_points = self.max_ability_points
            self.money += 100
        if self.race == "Mutant":
            self.damage += 1
            self.max_health += 5
            self.health = self.max_health
        if self.race == "Cyborg":
            self.armor += 1
            self.agility += 1

    def distribute_attribute_points(self):
        adjustable_attributes = ["Attack", "Agility", "Max Health", "Ability Points", "Skill Points"]
        points_left = 5
        while points_left > 0:
            print "You have: " + str(points_left) + " points left."
            for i in xrange(len(adjustable_attributes)):
                print str(i + 1) + ") " + adjustable_attributes[i]
            choice = int(raw_input())
            points_left -= 1
            if choice == 1:
                self.attack += 1
            elif choice == 2:
                self.agility += 1
            elif choice == 3:
                self.max_health += 5
                self.health = self.max_health
            elif choice == 4:
                self.max_ability_points += 1
                self.ability_points = self.max_ability_points
            elif choice == 5:
                self.skill_points += 1
            else:
                points_left += 1
                print "Invalid Input, enter a number 1 - " + str(len(adjustable_attributes))

    def generate_new_character(self):
        print "Creating a new character."
        print "Choose a name: "
        self.name = raw_input()
        print "Choose a profession"
        for i in xrange(len(self.list_of_professions)):
            print str(i+1) + ") " + self.list_of_professions[i]
        # TODO: add something that explains each profession
        choice = int(raw_input())
        self.profession = self.list_of_professions[choice-1]
        self.set_player_stats()
        print "Choose a race: "
        for i in xrange(len(self.list_of_races)):
            print str(i+1) + ") " + self.list_of_races[i]
        # TODO: put in something that explains pro/cons of each race
        choice = int(raw_input())
        self.race = self.list_of_races[choice-1]
        self.adjust_race_stats()
        self.distribute_attribute_points()


    def load_character(self):
        print "Feature not available"

    def set_opponent(self):
        self.name = "Squishbot"
        self.attack = 1
        self.dodge = 1
        self.damage = 1
        self.armor = 0
        self.max_health = 5
        self.health = self.max_health
        self.max_ability_points = 5
        self.ability_points = self.max_ability_points
        self.agility = 1
        self.is_dead = False
        self.technique_list = [techniques.Beep("player")]
        # Key is inventory object, val is qty
        self.inventory = {techniques.BeefJerky(): 5}

if __name__ == "__main__":
    print "Nothing to see here...."