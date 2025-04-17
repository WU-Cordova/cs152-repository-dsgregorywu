import sys
from datastructures.liststack import ListStack
class Menu:
    def __init__(self, menu_name, bistro_system):
        self.menu_name = menu_name
        self.bistro_system = bistro_system
        if menu_name in bistro_system.menus:
            self.options = bistro_system.menus[menu_name]
        else: raise ValueError(f"Menu '{menu_name}' not found in the bistro system.")


class Drink:
    """A Drink ordered from the Bearcat Bistro."""
    def __init__(self, bistro_system):
        self.bistro_system = bistro_system
        self.name = ""
        self.size = ""
        self.cost = float(0.0)
        self.base = ""
        self.fflavors = []
        self.sflavors = []
        self.addons = []
        self.teas = ""
        self.milk = ""
        self.espressodrink = ""
        self.dripdrink = ""
        self.noncoffee = ""

class Snack:
    """A snack ordered from the bistro."""
    def __init__(self, item, bistro_system):
        self.name = str(item)
        self.bistro_system = bistro_system 
        if item in self.bistro_system.snacks:
            self.item = item
            self.cost = self.bistro_system.snacks[item]
        else:
            raise IndexError("Item not available.")

class CustomerOrder:
    """A customer's order, including name, price, and each item ordered"""
    def __init__(self, name, bistro_system):
        self.price = 0.0
        self.items = []
        self.name = name
        self.bistro_system = bistro_system 
        self.drinkscreens = ListStack(data_type=Menu)

    def order_items(self):
        response = input("Would you like a (D)rink or (S)nack? ").strip().upper()
        print("    ")
        if response == "D":
            self.order_drink()
        elif response == "S":
            self.order_snack()

    def order_snack(self):
        print("Available Snacks:")
        snack_list = list(self.bistro_system.snacks.keys())
        for index, snack in enumerate(snack_list, start=1):
            print(f"{index}. {snack}")
        print("   ")
        while True:
            snack_choice = input("Please select a snack by number, or choose (B)ack or (Q)uit: ").strip().lower()
            if snack_choice == "q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif snack_choice == "b":
                self.bistro_system.homescreen()
                return
            elif snack_choice.isdigit():
                index = int(snack_choice) - 1
                if 0 <= index < len(snack_list):
                    snack_name = snack_list[index]
                    print(f"You selected: {snack_name}")
                    newsnack = Snack(snack_name, self.bistro_system)
                    while True:
                        response = input(f"Would you like to add {snack_name} to your order? (Y)es or (N)o? ").strip().lower()
                        if response == "y":
                            self.add_item(newsnack)
                            break
                        elif response == "n":
                            break
                        else:
                            print("Invalid response. Please try again.")
                    looping = True
                    while looping:
                        response = input("Would you like to order more? (Y)es or (N)o? ")
                        if response.upper() == "Y" or response.upper() == "N":
                            looping = False
                        else: print("Invalid response. Please try again.")
                    if response == "Y": self.order_items()
                    elif response == "N": self.complete_order()
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid selection. Please try again.")

    def complete_order(self):
        pass

    def order_drink(self):
        self.newdrink = Drink(self.bistro_system)
        self.bistro_system.print_numbered_menu({"Bases": self.bistro_system.bases})
        looping = True
        while looping:
            drink_choice = input("Please select a base by number.").strip()
            if drink_choice.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif drink_choice.upper() == "B": 
                print("Exiting the menu.")
                self.bistro_system.homescreen()
            elif drink_choice.isdigit():
                index = int(drink_choice) - 1
                if 0 <= index < len(self.bistro_system.bases):
                    selected_base = list(self.bistro_system.bases.keys())[index]
                    print(f"You selected: {selected_base}")
                    looping = False
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid input. Please try again..")
        self.newdrink.base = str(selected_base)
        if selected_base == "Drip": 
            self.choose_drip()
            self.choose_addons()
        elif selected_base == "Espresso": 
            self.choose_espresso()
            self.choose_milk
            self.choose_sflavors()
            self.choose_addons()
        elif selected_base == "Redbull": 
            self.choose_fflavors()
            self.choose_addons()
        elif selected_base == "Tea": 
            self.choose_tea()
            self.choose_addons()
        elif selected_base == "Lemonade": 
            self.choose_fflavors()
            self.choose_addons()
        else: raise IndexError("No such base available.")


    def choose_fflavors(self):
        self.bistro_system.print_numbered_menu({"Fruity Flavors": self.bistro_system.fflavors})
        looping = True
        while looping:
            response = input("Which flavor would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.upper == "N":
                flavor = None
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.fflavors) + 1 and response > 0:
                    flavor = self.bistro_system.fflavors[response -1]
                    if flavor in self.newdrink.fflavors: 
                        print("You've already ordered this flavor.")
                    else:
                        self.newdrink.fflavors.append(flavor)
                        self.newdrink.cost = self.newdrink.cost + 0.5 
                        looping = False
            else: print("Invalid response. Please try again.")
        if flavor is None:
            print("No flavor selected.")
            print("   ")
        else:
            print(f"You chose {flavor}.")
            print("  ")
            looping = True
            while looping:
                response = input("Would you like to add another flavor? ")
                if response.upper() == "Y" or response.upper() == "N": looping = False
                else: print("Invalid response. Please try again.")
            if response.upper() == "Y":
                self.choose_fflavors()
            
    def choose_sflavors(self):
        newscreen = Menu("Savory Flavors", self.bistro_system)
        self.drinkscreens.push(newscreen)
        newscreen.menu_name = "Savory Flavors"
        self.bistro_system.print_numbered_menu({"Savory Flavors": self.bistro_system.sflavors})
        looping = True
        while looping:
            response = input("Which flavor would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.upper == "N":
                flavor = None
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.sflavors) + 1 and response > 0:
                    flavor = self.bistro_system.sflavors[response - 1]
                    if flavor in self.newdrink.sflavors: 
                        print("You've already ordered this flavor.")
                    else:
                        self.newdrink.sflavors.append(flavor)
                        self.newdrink.cost = self.newdrink.cost + 0.5 
                        looping = False
            else: print("Invalid response. Please try again.")
        if flavor is  None:
            print("No flavor selected.")
            print("   ")
        else:
            print(f"You chose {flavor}.")
            print("   ")
            looping = True
            while looping:
                response = input("Would you like to add another flavor? ")
                if response.upper() == "Y": looping = False
                elif response.upper == "N": looping = False
                else: print("Invalid response. Please try again!")
            if response.upper() == "Y":
                self.choose_sflavors()
        
    def choose_milk(self):
        self.bistro_system.print_numbered_menu({"Milks": self.bistro_system.milk})
        looping = True
        while looping:
            response = input("Which milk would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.milklist) + 1 and response > 0:
                    milk = self.bistro_system.milk[response - 1]
                    self.newdrink.milk = milk
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.milk[milk] 
                    looping = False
            else: print("Invalid response. Please try again.")
        print(f"You chose {milk}.")
        print("    ")

    def choose_addons(self):
        self.bistro_system.print_numbered_menu({"Add Ons": self.bistro_system.addons})
        looping = True
        while looping:
            response = input("Would you like an Add On? Press N for None. ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                pass
            elif response.upper() == "N":
                addon = None
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.addons) + 1 and response > 0:
                    addon = self.bistro_system.addons[response - 1]
                    if addon in self.newdrink.addons: 
                        print("You've already ordered this Add On.")
                    else:
                        self.newdrink.addons.append(addon)
                        self.newdrink.cost = self.newdrink.cost + self.bistro_system.addons[addon]
                        looping = False
            else: print("Invalid response. Please try again.")
        if addon is not None:
            print(f"You chose {addon}.")
            looping = True
            while looping:
                response = input("Would you like to add another Add On?")
                if response.upper() == "Y" or response.upper == "N": looping = False
                else: print("Invalid response. Please try again.")
            if response.upper() == "Y":
                self.choose_addons()
        else: 
            print("No Add Ons selected.")
            print(" ")

    def choose_tea(self):
        self.bistro_system.print_numbered_menu({"Teas": self.bistro_system.teas})
        looping = True
        while looping:
            response = input("Which tea would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.teas) + 1 and response > 0:
                    tea = self.bistro_system.teas[response - 1] 
                    self.newdrink.teas = tea
                    looping = False
            else: print("Invalid response. Please try again.")
        print(f"You chose {tea}.")
        print("   ")

    def choose_espresso(self):
        self.bistro_system.print_numbered_menu({"Espresso Drinks": self.bistro_system.espressodrinks})
        looping = True
        while looping:
            response = input("Which drink would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.espressodrinks) + 1 and response > 0:
                    edrink = self.bistro_system.espressolist[response - 1]
                    self.newdrink.tea = edrink
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.espressodrinks[edrink] 
                    looping = False
            else: print("Invalid response. Please try again.")
        if edrink == "Mocha":
            self.newdrink.sflavors.append("Chocolate")
        elif edrink == "White Mocha":
            self.newdrink.sflavors.append("White Chocolate")
        print(f"You chose {edrink}.")
        print("  ")

    def choose_drip(self):
        self.bistro_system.print_numbered_menu({"Drip Options": self.bistro_system.dripoptions})
        looping = True
        while looping:
            response = input("Which drink would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.dripoptions) + 1 and response > 0:
                    drip = self.bistro_system.driplist[response - 1]
                    self.newdrink.dripdrink = drip
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.dripoptions[drip] 
                    looping = False
            else: print("Invalid response. Please try again.")
        print(f"You chose {drip}.")
        print("   ")

    def choose_noncoffee(self):
        self.bistro_system.print_numbered_menu({"Non Coffee": self.bistro_system.noncoffee})
        looping = True
        while looping:
            response = input("Which drink would you like? ")
            if response.upper() == "Q": 
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper == "B":
                pass
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.noncoffee) + 1:
                    response = self.bistro_system.noncoffeelist[response - 1]
                    self.newdrink.dripdrink = response
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.dripoptions[response] 
                    looping = False
            else: print("Invalid response. Please try again.")
        print(f"You chose {response}.")

    def add_item(self, item):
        if not isinstance(item, (Snack, Drink)):
            raise TypeError("Item not of correct type.")
        self.items.append(item)
        self.price += item.cost
        printstr = "Order for "
        printstr += str(self.name)
        printstr += ": "
        for item in self.items:
            printstr += str(item.name)
            printstr += ", "
        printstr = printstr[0:-2]
        print(printstr)
        print("   ")
        self.order_items()

class BistroSystem:
    """Defines the system with which the bistro uses to run."""
    def __init__(self):
        self.reports = {}
        self.openorders = []
        self.user = ""
        self.bases = {}
        self.snacks = []
        self.dripoptions = {}
        self.users = {"Derec": "CS152"}
        self.espressolist = ["Americano", "Latte", "Mocha", "White Mocha"]
        self.driplist = ["Black Hole", "House", "Iced", "Specialty"]
        self.milklist = ["Almond", "Coconut", "Darjeeling", "Earl Grey", "Jasmine", "Lemongrass", "Matcha", "Oolong", "Rooibos"]
        self.noncoffeelist = ["Berry Lemonade", "Hot Chocolate", "Italian Soda", "Steamer", "Redbull Fusion"]
        self.bases = {"Drip": 2.25, "Espresso": 3.5, "Lemonade": 3.50, "Redbull": 4.25, "Tea": 3.5}
        self.fflavors = ["Blackberry", "Blueberry", "Blue Raspberry", "Grape", "Grapefruit", "Lavender", "Lime", "Mango", 
                        "Passionfruit", "Peach", "Pear", "Pomegranate", "Pineapple", "Raspberry", "Strawberry", "Watermelon"]
        self.sflavors = ["Chocolate", "Caramel", "Hazelnut", "Pumpkin Spice", "Vanilla", "Irish Cream", "White Chocolate"]
        self.teas = ["Chai", "Chamomile", "Darjeeling", "Earl Grey", "Jasmine", "Lemongrass", "Matcha", "Oolong", "Rooibos"]
        self.addons = {"Cold Foam": 1.00, "Espresso Shot": 2.00, "Flavor": 0.50, "Whipped Cream": 0.50}
        self.milk = {"Almond": 0.50, "Coconut": 0.50, "Nonfat": 0, "Oat": 0.50, "Soy": 0.50, "Whole": 0}
        self.espressodrinks = {"Americano": 3.75, "Latte": 4.50, "Mocha": 5.00, "White Mocha": 5.00}
        self.dripoptions = {"Black Hole": 4.50, "House": 2.25, "Iced": 3.00, "Specialty": 2.25}
        self.noncoffee = {"Berry Lemonade": 4.00, "Hot Chocolate": 3.50, "Italian Soda": 3.50, "Steamer": 3.50, "Redbull Fusion": 4.50}
        self.snacks = {"Bagel": 2.75, "Chocolate Chip Cookie": 1.50, "Curry Pocket": 5.00, "Sugar Cookie": 2.00, "Quesadilla": 3.25, "Pizza": 2.75}
        self.menus = {"Add Ons": self.addons, "Bases": self.bases, "Drip Options": self.dripoptions, "Espresso Drinks": self.espressodrinks, 
                    "Fruity Flavors": self.fflavors, "Milks": self.milk, "Non Coffee": self.noncoffee, 
                    "Savory Flavors": self.sflavors, "Snacks": self.snacks, "Teas": self.teas}
        self.allmenus = {"Add Ons": self.addons, "Bases": self.bases, "Drip Options": self.dripoptions, "Espresso Drinks": self.espressodrinks, 
                    "Fruity Flavors": self.fflavors, "Milks": self.milk, "Non Coffee": self.noncoffee, 
                    "Savory Flavors": self.sflavors, "Snacks": self.snacks, "Teas": self.teas, 'Menus': self.menus}

    def useraccess(self):
        while True:
            username = input("Welcome, Bearcat Bistro Employee! Please Enter Your Username: ")
            if username in self.users:
                break
            else:
                print("There is no such user. Please try again.")        
        while True:
            password = input("Please enter your password: ")
            if self.users.get(username) == password: break
            else: print("Incorrect password. Please try again.")
        self.user = username

    def homescreen(self):
        print(f"Welcome to the Bearcat Bistro, {self.user}!")
        print("    ")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Order")
        print("4. Mark Day as Complete")
        print("5. View End of Day Report")
        print("6. Exit")
        print("    ")
        response = input("Please select an option. ")
        if response == "1":
            self.display_menu()
        elif response == "2":
            self.begin_order()
        elif response == "3":
            self.view_orders()
        elif response == "4":
            self.view_orders()
        elif response == "5":
            self.view_report()
        elif response == "6": sys.exit()

    def print_menu(self, menu):
        for category, items in menu.items():
            print(category)
            for item in items:
                print(f"  - {item}")
            print()

    def display_menu(self):
        while True:
            printstr = "Menus: "
            tracker = 0
            menu_keys = list(self.menus.keys())        
            for menu in menu_keys: 
                tracker += 1
                printstr += f"{tracker}: {menu}, "
            printstr = printstr[:-2]
            print(printstr)
            response = input("Which Menu would you like to view? [B]ack to options, [Q]uit: ").strip().upper()
            print("   ")
            special_commands = {
                'B': "back",
                'Q': "quit"}
            if response.isdigit():
                index = int(response) - 1
                if 0 <= index < len(menu_keys):
                    selected_menu = menu_keys[index]
                    self.print_menu({selected_menu: self.menus[selected_menu]})
                else:
                    print("Invalid selection. Please choose a valid menu number.")
            elif response in special_commands:
                action = special_commands[response]
                if action == "back":
                    print("Going back to the previous menu.")
                    self.homescreen()
                elif action == "quit":
                    print("Exiting Bearcat Bistro.")
                    break  
            else:
                print("Invalid selection. Please enter a valid menu number or command. ")

    def print_numbered_menu(self, menu):
        for category, items in menu.items():
            print(category)
            for index, item in enumerate(items, start=1):
                print(f"  {index}. {item}")
            print()

    def begin_order(self):
        ordername = input("What name would you like to use for your order? ")
        neworder = CustomerOrder(ordername, self) 
        neworder.order_items()

    def view_orders(self):
        pass

    def eod(self):
        pass

    def view_report(self):
        pass

        def run_bistro():
            """The main function to use the program."""

if __name__ == '__main__':
    game = BistroSystem()
    game.useraccess()
    game.homescreen()