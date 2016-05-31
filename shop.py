import techniques

class Shop():
    def __init__(self):
        # TODO: turn this into a function that references a database
        self.inventory = [techniques.BeefJerky()]
        self.sell_markdown = 0.5

    def main_menu(self, player_group):
        while True:
            print "Welcome to the shop, please select an option:"
            print "1) Buy Item/Equipment"
            print "2) Sell inventory"
            print "3) Quit"
            print
            for player in player_group:
                print player.name + " has " + str(player.money)
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
        for inventory_item in self.inventory:
            print str(inventory_idx + 1) + ") " + inventory_item.name + "\tCost: " + str(inventory_item.money_cost)
            inventory_idx +=1
        print "Enter the # of the inventory item you want."
        item_choice = int(raw_input())
        print "Enter how many you would like to buy."
        qty_choice = int(raw_input())
        print "Who is this for?"
        for player in player_group:
            print player.name
        player_choice = raw_input()
        for player in player_group:
            if player_choice == player.name:
                item_to_add = self.inventory[item_choice-1]
                # Add if item already exists in inventory
                try:
                    player.inventory[item_to_add] +=1
                # Add item if it's not in inventory
                except KeyError:
                    player.inventory[item_to_add] = 1
                    # TODO: add error guard against spending more than you have
                player.money -= item_to_add.money_cost

    def sell_menu(self, player_group):
        tmp_inventory_dict = {}
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
            tmp_inventory_dict[inventory_item.name] = inventory_item
        print "Type the name of the item you want to sell"
        item_choice = raw_input()
        print "Enter how many you would like to sell."
        # TODO: put guard around selling more than you have
        qty_choice = int(raw_input())
        item_to_sell = tmp_inventory_dict[item_choice]
        player.inventory[item_to_sell] -= qty_choice
        # Delete the item from inventory if
        if player.inventory[item_to_sell] ==10:
            del player.inventory[item_to_sell]
