import sys
from datastructures.liststack import ListStack
from datastructures.deque import Deque


class Menu:
    def __init__(self, menu_name, bistro_system):
        self.menu_name = menu_name
        self.bistro_system = bistro_system
        if menu_name in bistro_system.menus:
            self.options = bistro_system.menus[menu_name]
        else:
            raise ValueError(f"Menu '{menu_name}' not found in the bistro system.")

class Drink:
    """A Drink ordered from the Bearcat Bistro."""
    def __init__(self, bistro_system):
        self.bistro_system = bistro_system
        self.name = ""
        self.size = ""
        self.timer = int
        self.cost = float(0.00)
        self.base = ""
        self.fflavors = []
        self.sflavors = []
        self.addons = []
        self.teas = ""
        self.milk = ""
        self.espressodrink = ""
        self.dripdrink = ""
        self.noncoffee = ""
        self.temp = ""

    def display_drink(self):
        self.drinkstr = self.size
        if self.temp and self.base != "Redbull" and self.base != "Lemonade" and self.base != "Tea":
            self.drinkstr += f" {self.temp}"
        for flavor_list in [self.fflavors, self.sflavors]:
            if flavor_list:
                self.drinkstr += " " + ", ".join(flavor_list)
        if self.espressodrink:
            self.drinkstr += f" {self.espressodrink}"
        if self.teas:
            self.drinkstr += f" {self.teas} Tea"
        if self.noncoffee:
            self.drinkstr += f" {self.noncoffee}"
        if self.base == "Redbull" or self.base == "Lemonade":
            self.drinkstr += f" {self.base}"
        if self.dripdrink:
            if self.dripdrink == "Black Hole":
                self.drinkstr += f" {self.dripdrink}"
            else:
                self.drinkstr += f" {self.dripdrink} Coffee"
        if self.milk or self.addons:
            self.drinkstr += " with "
            milk_addons = []
            if self.base == "Espresso" and self.milk:
                milk_addons.append(self.milk + " Milk")
            milk_addons += [str(addon) for addon in self.addons]
            if milk_addons:
                self.drinkstr += ", ".join(milk_addons[:-1])
                if len(milk_addons) > 1:
                    self.drinkstr += " and " + milk_addons[-1]
                else:
                    self.drinkstr += milk_addons[0]

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
        looping = True
        while looping:
            if self.items == []:
                response = input("Would you like a (D)rink or (S)nack? ").strip().upper()
                print("    ")
            else: 
                response = input("Would you like a (D)rink, a (S)nack, or to (C)omplete your order? ").strip().upper()
                print("    ")
            if response == "D":
                self.order_drink()
            elif response == "S":
                self.order_snack()
            elif response == "C" and self.items != []:
                self.complete_order()
            else: print("Invalid response. Please try again.")

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
                    print(f"You chose: {snack_name}")
                    newsnack = Snack(snack_name, self.bistro_system)
                    while True:
                        response = input(f"Would you like to add {snack_name} to your order? (Y)es or (N)o? ").strip().lower()
                        if response == "y":
                            self.add_item(newsnack)
                            break
                        elif response == "n":
                            printstr = "Order for "
                            printstr += str(self.name)
                            printstr += ": "
                            for item in self.items:
                                if type(item) == Drink:
                                    printstr += str(item.drinkstr)
                                elif type(item) == Snack:
                                    printstr += str(item.name)
                                printstr += ", "
                            printstr = printstr[0:-2]
                            print(printstr)
                            print("   ")
                            break
                        else:
                            print("Invalid response. Please try again.")
                    self.order_items()
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid selection. Please try again.")

    def complete_order(self):
        print(f"Order for {self.name} Confimed! Your Reciept:")
        for item in self.items:
            self.bistro_system.reports[item] = item.cost
            if type(item) == Snack: print(item.name)
            elif type(item) == Drink: print(item.drinkstr)
        print(f"You Paid: ${self.price}")
        print(f"Your Barista: {self.bistro_system.user}")
        print(" ")
        self.bistro_system.allorders.enqueue(self)
        self.bistro_system.orders.enqueue(self)
        self.bistro_system.homescreen()

        
    def add_to_order(self):
        if self.newdrink.espressodrink == "White Mocha" and "White Chocolate" in self.newdrink.sflavors:
            self.newdrink.sflavors.remove("White Chocolate")
        if self.newdrink.espressodrink == "Mocha" and "Chocolate" in self.newdrink.sflavors:
            self.newdrink.sflavors.remove("Chocolate")
        self.newdrink.display_drink()
        print(f"Your drink: {self.newdrink.drinkstr}")
        looping = True
        while looping:
            response = input("Would you like to add this to your order? (Y)es or (N)o? ")
            print(" ")
            if response.upper() == "Y":
                print("Item added to your order!")
                self.drinkscreens.clear()
                self.add_item(self.newdrink)
            elif response.upper() == "N":
                self.drinkscreens.clear()
                print("Returning to menu.")
                self.drinkscreens.clear()
                self.order_items()
            else:
                print("Invalid choice. Please try again.")

    def order_drink(self):
        self.newdrink = Drink(self.bistro_system)
        self.choose_base()

    def choose_base(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Bases": self.bistro_system.bases})
            drink_choice = input("Please select a base. ").strip()
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
                    print(f"You chose: {selected_base}")
                    print(" ")
                    self.newdrink.cost += int(self.bistro_system.bases[selected_base])
                    newscreen = Menu("Bases", self.bistro_system)
                    self.drinkscreens.push(newscreen)
                    looping = False
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid input. Please try again..")
        self.newdrink.base = str(selected_base)
        if selected_base == "Drip":
            self.choose_drip()
            self.choose_temp()
            self.choose_addons()
            self.choose_size()
        elif selected_base == "Espresso":
            self.choose_espresso()
            self.choose_temp()
            if self.newdrink.espressodrink != "Americano":
                self.choose_milk()
            self.choose_sflavors()
            self.choose_addons()
            self.choose_size()
        elif selected_base == "Redbull":
            self.choose_fflavors()
            self.choose_addons()
            self.choose_size()
        elif selected_base == "Tea":
            self.choose_tea()
            self.choose_addons()
            self.choose_size()
        elif selected_base == "Lemonade":
            self.choose_fflavors()
            self.choose_addons()
            self.choose_size()
        else:
            raise IndexError("No such base available.")
        self.add_to_order()

    def back(self):
        if self.drinkscreens.empty:
            print("No previous menu to return to.")
            return
        try:
            screen = self.drinkscreens.pop()
        except IndexError:
            print("Error: Tried to pop from an empty stack.")
            return
        if screen.menu_name == "Fruity Flavors":
            if self.newdrink.fflavors != []:
                removed_item = self.newdrink.fflavors.pop()
                print(f"Removing last fruity flavor choice: {removed_item}")
                self.newdrink.cost -= .5
            self.choose_fflavors()
        elif screen.menu_name == "Savory Flavors":
            if self.newdrink.sflavors != []:
                removed_item = self.newdrink.sflavors.pop()
                print(f"Removing last savory flavor choice: {removed_item}")
                self.newdrink.cost -= .5
            self.choose_sflavors()
        elif screen.menu_name == "Add Ons":
            if self.newdrink.addons != []:
                removed_item = self.newdrink.addons.pop()
                self.newdrink.cost -= float(self.bistro_system.addons[removed_item])
                print(f"Removing last addon choice: {removed_item}")
            self.choose_addons()
        elif screen.menu_name == "Milks":
            if self.newdrink.milk:
                removed_item = self.newdrink.milk
                print(f"Removing milk choice: {self.newdrink.milk}")
                self.newdrink.milk = ""
                self.newdrink.cost -= float(self.bistro_system.milk[removed_item])
            self.choose_milk()
        elif screen.menu_name == "Espresso Drinks":
            if self.newdrink.espressodrink:
                removed_item = self.newdrink.espressodrink
                print(f"Removing Drink Choice {self.newdrink.espressodrink}")
                self.newdrink.espressodrink = ""
                self.newdrink.cost -= float(self.bistro_system.espressodrinks[removed_item])
                self.choose_espresso()
        elif screen.menu_name == "Teas":
            if self.newdrink.teas:
                print(f"Removing Tea Choice {self.newdrink.teas}")
                self.newdrink.teas = ""
                self.choose_tea()
        elif screen.menu_name == "Non Coffee":
            if self.newdrink.noncoffee:
                removed_item = self.newdrink.noncoffee
                print(f"Removing Drink Choice {self.newdrink.noncoffee}")
                self.newdrink.noncoffee = ""
                self.newdrink.cost -= float(self.bistro_system.noncoffee[removed_item])
                self.choose_noncoffee()
        elif screen.menu_name == "Bases":
            if self.newdrink.base:
                removed_item = self.newdrink.base
                print(f"Removing Base Choice {self.newdrink.base}")
                self.newdrink.base = ""
                self.newdrink.cost -= float(self.bistro_system.bases[removed_item])
                self.choose_base()
        elif screen.menu_name == "Drip Options":
            if self.newdrink.dripdrink:
                print(f"Removing Drink Choice {self.newdrink.dripdrink}")
                self.newdrink.cost -= float(self.bistro_system.dripoptions[removed_item])
                self.newdrink.dripdrink = ""
                self.choose_drip()
        elif screen.menu_name == "Temperatures":
            if self.newdrink.temp:
                print(f"Removing Temperature Choice {self.newdrink.temp}")
                self.newdrink.temp = ""
                self.choose_temp()
        elif screen.menu_name == "Sizes":
            if self.newdrink.size:
                removed_item = self.newdrink.size
                print(f"Removing Size Choice {self.newdrink.size}")
                self.newdrink.cost -= float(self.bistro_system.sizes[removed_item])
                self.newdrink.size = ""
                self.choose_size()


    def choose_fflavors(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Fruity Flavors": self.bistro_system.fflavors})
            response = input("Which flavor would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.upper == "N":
                flavor = None
                newscreen = Menu("Fruity Flavors", self.bistro_system)
                self.drinkscreens.push(newscreen)
            elif response.isdigit() and int(response) > len(self.bistro_system.fflavors):
                print("Invalid response. Please try again.")
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.fflavors) + 1 and response > 0:
                    flavor = self.bistro_system.fflavors[response - 1]
                    if flavor in self.newdrink.fflavors:
                        print("You've already ordered this flavor.")
                    else:
                        self.newdrink.fflavors.append(flavor)
                        self.newdrink.cost = self.newdrink.cost + 0.5
                        looping = False
            else:
                print("Invalid response. Please try again.")
        if flavor is None:
            print("No flavor selected.")
            print("   ")
        else:
            print(f"You chose {flavor}.")
            newscreen = Menu("Fruity Flavors", self.bistro_system)
            self.drinkscreens.push(newscreen)
            print("  ")
            looping = True
            while looping:
                response = input("Would you like to add another flavor? ")
                if response.upper() == "Y" or response.upper() == "N" or response.upper() == "B":
                    looping = False
                else:
                    print("Invalid response. Please try again.")
            if response.upper() == "Y":
                self.choose_fflavors()
            elif response.upper() == "B":
                self.back()

    def choose_size(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Sizes": self.bistro_system.sizes})
            response = input("What size would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                index = int(response) - 1
                if 0 <= index < len(self.bistro_system.sizes):
                    self.newdrink.size = list(self.bistro_system.sizes.keys())[index]
                    looping = False
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid response. Please try again.")
        print(f"You chose {self.newdrink.size}")
        print(" ")
        newscreen = Menu("Sizes", self.bistro_system)
        if self.newdrink.size == "Medium": self.newdrink.cost += .25
        if self.newdrink.size == "Large": self.newdrink.cost += .5
        self.drinkscreens.push(newscreen)

    def choose_temp(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Temperatures": self.bistro_system.temperatures})
            response = input("Would you like that (I)ced or (H)ot? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                index = int(response) - 1
                if 0 <= index < len(self.bistro_system.temperatures):
                    self.newdrink.temp = list(self.bistro_system.temperatures.keys())[index]
                    looping = False
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid response. Please try again.")
        print(f"You chose {self.newdrink.temp}")
        print(" ")
        newscreen = Menu("Temperatures", self.bistro_system)
        self.drinkscreens.push(newscreen)

    def choose_sflavors(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Savory Flavors": self.bistro_system.sflavors})
            response = input("Which flavor would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.upper == "N":
                flavor = None
                newscreen = Menu("Savory Flavors", self.bistro_system)
                self.drinkscreens.push(newscreen)
            elif response.isdigit() and int(response) > len(self.bistro_system.sflavors):
                print("Invalid response. Please try again.")
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
            else:
                print("Invalid response. Please try again.")
        if flavor is None:
            print("No flavor selected.")
            print("   ")
        else:
            print(f"You chose {flavor}.")
            newscreen = Menu("Savory Flavors", self.bistro_system)
            self.drinkscreens.push(newscreen)
            print("   ")
            looping = True
            while looping:
                response = input("Would you like to add another flavor? ")
                if response.upper() == "Y":
                    looping = False
                elif response.upper() == "N":
                    looping = False
                else:
                    print("Invalid response. Please try again!")
            if response.upper() == "Y":
                self.choose_sflavors()

    def choose_milk(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Milks": self.bistro_system.milk})
            response = input("Which milk would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.milklist) + 1 and response > 0:
                    milk = self.bistro_system.milklist[response - 1]
                    self.newdrink.milk = milk
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.milk[milk]
                    looping = False
            else:
                print("Invalid response. Please try again.")
        print(f"You chose {milk}.")
        newscreen = Menu("Milks", self.bistro_system)
        self.drinkscreens.push(newscreen)
        print("    ")

    def choose_addons(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Add Ons": self.bistro_system.addons})
            response = input("Would you like an Add On? Press N for None. ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.upper() == "N":
                addon = None
                newscreen = Menu("Add Ons", self.bistro_system)
                self.drinkscreens.push(newscreen)
                looping = False
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.addons) + 1 and response > 0:
                    addon = self.bistro_system.addonlist[response - 1]
                    if addon in self.newdrink.addons:
                        print("You've already ordered this Add On.")
                    else:
                        self.newdrink.addons.append(addon)
                        self.newdrink.cost = self.newdrink.cost + self.bistro_system.addons[addon]
                        looping = False
            else:
                print("Invalid response. Please try again.")
        if addon is not None:
            print(f"You chose {addon}.")
            newscreen = Menu("Add Ons", self.bistro_system)
            self.drinkscreens.push(newscreen)
            looping = True
            while looping:
                response = input("Would you like to add another Add On? ")
                print(" ")
                if response.upper() == "Y":
                    self.choose_addons()
                    looping = False
                elif response.upper() == "N":
                    looping = False
                elif response.upper() == "B":
                    self.back()
                    looping = False
                else:
                    print("Invalid response. Please try again.")
        else:
            print("No Add Ons selected.")
            print(" ")

    def choose_tea(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Teas": self.bistro_system.teas})
            response = input("Which tea would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.teas) + 1 and response > 0:
                    tea = self.bistro_system.teas[response - 1]
                    self.newdrink.teas = tea
                    looping = False
            else:
                print("Invalid response. Please try again.")
        print(f"You chose {tea}.")
        newscreen = Menu("Teas", self.bistro_system)
        self.drinkscreens.push(newscreen)
        print("   ")

    def choose_espresso(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Espresso Drinks": self.bistro_system.espressodrinks})
            response = input("Which drink would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.espressodrinks) + 1 and response > 0:
                    edrink = self.bistro_system.espressolist[response - 1]
                    self.newdrink.espressodrink = edrink
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.espressodrinks[edrink]
                    looping = False
            else:
                print("Invalid response. Please try again.")
        if edrink == "Mocha":
            self.newdrink.sflavors.append("Chocolate")
        elif edrink == "White Mocha":
            self.newdrink.sflavors.append("White Chocolate")
        print(f"You chose {edrink}.")
        newscreen = Menu("Espresso Drinks", self.bistro_system)
        self.drinkscreens.push(newscreen)
        print("  ")

    def choose_drip(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Drip Options": self.bistro_system.dripoptions})
            response = input("Which drink would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.dripoptions) + 1 and response > 0:
                    drip = self.bistro_system.driplist[response - 1]
                    self.newdrink.dripdrink = drip
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.dripoptions[drip]
                    looping = False
            else:
                print("Invalid response. Please try again.")
        print(f"You chose {drip}.")
        newscreen = Menu("Drip Options", self.bistro_system)
        self.drinkscreens.push(newscreen)
        print("   ")


    def choose_noncoffee(self):
        looping = True
        while looping:
            self.bistro_system.print_numbered_menu({"Non Coffee": self.bistro_system.noncoffee})
            response = input("Which drink would you like? ")
            if response.upper() == "Q":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif response.upper() == "B":
                self.back()
            elif response.isdigit():
                response = int(response)
                if response <= len(self.bistro_system.noncoffee) + 1:
                    response = self.bistro_system.noncoffeelist[response - 1]
                    self.newdrink.dripdrink = response
                    self.newdrink.cost = self.newdrink.cost + self.bistro_system.dripoptions[response]
                    looping = False
            else:
                print("Invalid response. Please try again.")
        print(f"You chose {response}.")
        newscreen = Menu("Non Coffee", self.bistro_system)
        self.drinkscreens.push(newscreen)
        newscreen.menu_name = "Non Coffee"
        print("  ")

    def add_item(self, item):
        if not isinstance(item, (Snack, Drink)):
            raise TypeError("Item not of correct type.")
        self.items.append(item)
        self.price += item.cost
        printstr = "Order for "
        printstr += str(self.name)
        printstr += ": "
        for item in self.items:
            if type(item) == Drink:
                printstr += str(item.drinkstr)
            elif type(item) == Snack:
                printstr += str(item.name)
            printstr += ", "
        printstr = printstr[0:-2]
        print(printstr)
        print("   ")
        self.order_items()

class BistroSystem:
    """Defines the system with which the bistro uses to run."""
    def __init__(self):
        self.revenue = int(0)
        self.orders = Deque(data_type=CustomerOrder)
        self.allorders = Deque(data_type=CustomerOrder)
        self.reports = {}
        self.openorders = []
        self.user = ""
        self.bases = {}
        self.snacks = []
        self.dripoptions = {}
        self.users = {"Derec": "CS152"}
        self.addonlist = ["Cold Foam", "Espresso Shot", "Whipped Cream"]
        self.espressolist = ["Americano", "Latte", "Mocha", "White Mocha"]
        self.driplist = ["Black Hole", "House", "Iced", "Specialty"]
        self.milklist = ["Almond", "Coconut", "Nonfat", "Oat", "Soy", "Whole"]
        self.noncoffeelist = ["Berry Lemonade", "Hot Chocolate", "Italian Soda", "Steamer", "Redbull Fusion"]
        self.bases = {"Drip": 2.25, "Espresso": 3.5, "Lemonade": 3.50, "Redbull": 4.25, "Tea": 3.5}
        self.fflavors = ["Blackberry", "Blueberry", "Blue Raspberry", "Grape", "Grapefruit", "Lavender", "Lime", "Mango",
                        "Passionfruit", "Peach", "Pear", "Pomegranate", "Pineapple", "Raspberry", "Strawberry", "Watermelon"]
        self.sflavors = ["Chocolate", "Caramel", "Hazelnut", "Pumpkin Spice", "Vanilla", "Irish Cream", "White Chocolate"]
        self.teas = ["Chai", "Chamomile", "Darjeeling", "Earl Grey", "Jasmine", "Lemongrass", "Matcha", "Oolong", "Rooibos"]
        self.addons = {"Cold Foam": 1.00, "Espresso Shot": 2.00, "Whipped Cream": 0.50}
        self.milk = {"Almond": 0.50, "Coconut": 0.50, "Nonfat": 0, "Oat": 0.50, "Soy": 0.50, "Whole": 0}
        self.espressodrinks = {"Americano": 3.75, "Latte": 4.50, "Mocha": 5.00, "White Mocha": 5.00}
        self.dripoptions = {"Black Hole": 4.50, "House": 2.25, "Specialty": 2.25}
        self.noncoffee = {"Berry Lemonade": 4.00, "Hot Chocolate": 3.50, "Italian Soda": 3.50, "Steamer": 3.50, "Redbull Fusion": 4.50}
        self.snacks = {"Bagel": 2.75, "Chocolate Chip Cookie": 1.50, "Curry Pocket": 5.00, "Sugar Cookie": 2.00, "Quesadilla": 3.25, "Pizza": 2.75}
        self.sizes = {"Small": 0.0, "Medium": 0.5, "Large": 1.0}
        self.temperatures = {"Iced": 0.0, "Hot": 0.0}
        self.menus = {"Add Ons": self.addons, "Bases": self.bases, "Drip Options": self.dripoptions, "Espresso Drinks": self.espressodrinks,
                    "Fruity Flavors": self.fflavors, "Milks": self.milk, "Non Coffee": self.noncoffee,
                    "Savory Flavors": self.sflavors, "Snacks": self.snacks, "Teas": self.teas, "Sizes": self.sizes, "Temperatures": self.temperatures}
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
            if self.users.get(username) == password:
                break
            else:
                print("Incorrect password. Please try again.")
        self.user = username

    def homescreen(self):
        print(f"Welcome to the Bearcat Bistro, {self.user}!")
        print("    ")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Order as Complete")
        print("5. View End of Day Report")
        print("6. Exit")
        print("    ")
        looping = True
        while looping:
            response = input("Please select an option. ")
            if response == "1":
                self.display_menu()
            elif response == "2":
                print(" ")
                self.begin_order()
            elif response == "3":
                self.view_orders()
            elif response == "4":
                self.mark_order_as_complete()
            elif response == "5":
                self.view_report()
            elif response == "6":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            else: print("Invalid response. Please try again.")

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

    def mark_order_as_complete(self):
        ordercompleted = self.orders.dequeue()
        print(f"Order Up for {ordercompleted.name}!")
        for item in ordercompleted.items:
            if type(item) == Snack: print(item.name)
            elif type(item) == Drink: print(item.drinkstr)
        self.homescreen()

    def print_numbered_menu(self, menu):
        for category, items in menu.items():
            print(category)
            for index, item in enumerate(items, start=1):
                print(f"  {index}. {item}")
            print()

    def begin_order(self):
        ordername = input("What name would you like to use for your order? ")
        print(" ")
        neworder = CustomerOrder(ordername, self)
        neworder.order_items()

    def view_orders(self):
        print(" ")
        if len(self.orders) == 0:
            print("There are no open orders.")
        else:
            for i in range(len(self.orders)):
                order = self.orders.dequeue()
                if not isinstance(order, CustomerOrder): raise TypeError("Dequed item is not of correct type.")
                print(f"Order for {order.name} - ${order.price}")
                for item in order.items:
                    if type(item) == Drink:
                        print(f"{item.drinkstr} - ${item.cost}")
                    elif type(item) == Snack:
                        print(f"{item.name} - ${item.cost}")
                print(" ")
                self.orders.enqueue(order)
        self.homescreen()
    
    def view_report(self):
        print(" ")
        temp_storage = Deque(data_type=CustomerOrder)
        order_list = []
        while not self.allorders.empty():
            order = self.allorders.dequeue()
            order_list.append(order)
            temp_storage.enqueue(order)
        while not temp_storage.empty():
            self.orders.enqueue(temp_storage.dequeue())
        print("Today's Sales")
        print(" ")
        for order in order_list:
            self.allorders.enqueue(order)
            print(f"Order for {order.name} - ${order.price}:")
            for item in order.items:
                if type(item) == Snack:
                    print(f"{item.name} - ${item.cost}")
                elif type(item) == Drink:
                    print(f"{item.drinkstr} - ${item.cost}")
            print(" ")
        print(f"Account User: {self.user}")
        print(" ")
        self.homescreen()

if __name__ == '__main__':
    game = BistroSystem()
    game.useraccess()
    game.homescreen()
