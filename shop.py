import techniques

class Shop():
    def __init__(self):
        # TODO: turn this into a function that references a database
        self.shop_inventory = [techniques.BeefJerky()]
        self.sell_markdown = 0.5

    def main_menu(self, player_group):
        while True:
            print "Welcome to the shop, please select an option:"
            print "1) Buy Item/Equipment"
            print "2) Sell inventory"
            print "3) Quit"
            print
            for player in player_group:
                print player.name + " has " + str(player.money) + " money."
            print
            choice = int(raw_input())
            if choice == 1:
                self.buy_menu(player_group)
            elif choice == 2:
                self.sell_menu(player_group)
            elif choice == 3:
                return

    def buy_menu(self, player_group):
        tmp_inventory_dict = {}
        print "Welcome to the buy menu."
        print "Please select an item you wish to buy."
        print
        inventory_idx = 0
        for inventory_item in self.shop_inventory:
            print str(inventory_idx + 1) + ") " + inventory_item.name + "\tCost: " + str(inventory_item.money_cost)
            inventory_idx +=1
        print "Enter the # of the inventory item you want."
        item_choice = int(raw_input())
        print "Enter how many you would like to buy."
        qty_choice = int(raw_input())
        print "Who is this for?"
        for player in player_group:
            print player.name
        print "Type the player name"
        player_choice = raw_input()
        item_match = False
        for player in player_group:
            if player_choice != player.name:
                continue
            item_to_add = self.shop_inventory[item_choice - 1]
            for item in player.inventory:
                if item_to_add.name == item.name:
                    player.inventory[item] += qty_choice
                    item_match = True
        if not item_match:
            player.inventory[item_to_add] = qty_choice

        # TODO: add error guard against spending more than you have
        player.money -= (item_to_add.money_cost * qty_choice)

    def sell_menu(self, player_group):
        tmp_inventory = []
        print "Welcome to the sell menu."
        print "Who is this for?"
        for player in player_group:
            print player.name
        player_choice = raw_input()
        for player in player_group:
            if player.name == player_choice:
                selected_player = player
        print "Please select an item you wish to sell."
        print
        for inventory_item in selected_player.inventory:
            print inventory_item.name + "\tSale Price: " + str(inventory_item.money_cost * self.sell_markdown) + "\tQty: " + str(selected_player.inventory[inventory_item])
            tmp_inventory.append(inventory_item)
        print "Type the name of the item you want to sell"
        item_choice = raw_input()
        print "Enter how many you would like to sell."
        # TODO: put guard around selling more than you have
        qty_choice = int(raw_input())
        for inventory_item in selected_player.inventory:
            if item_choice == inventory_item.name:
                player.inventory[inventory_item] -= qty_choice
                player.money += (int(inventory_item.money_cost * self.sell_markdown) * qty_choice)
