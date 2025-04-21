from datastructures.liststack import ListStack
from projects.project3.program import Drink, Menu, Snack
import sys


class CustomerOrder:
    """A customer's order, including name, price, and each item ordered"""
    def __init__(self, name, bistro_system):
        self.price = 0.0
        self.items = []
        self.name = name
        self.bistro_system = bistro_system
        self.drinkscreens = ListStack(data_type=Menu)

    def order_items(self):
        """Prompts the user to order either a drink or snack."""
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
        """Allows the user to order a snack and add it to their order."""
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
        """Completes a customer order and sends it to the Open Orders Deque."""
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
        """Prompts the user to add or remove their created drink from their order."""
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
        """Defines a drink."""
        self.newdrink = Drink(self.bistro_system)
        self.choose_base()

    def choose_base(self):
        """Allows the user to select a base for their drink."""
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
        """Allows the user to go "back" while in the drink building part of the menu."""
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
        """Chooses fruity flavors for a drink."""
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
        """Allows the user to choose between Small, Medium, and Large size for their drink."""
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
        """Allows users to choose if they want their drink hot or iced."""
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
        """Allows users to choose savory flavors for their drink."""
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
        """Allows users to choose what type of milk they want in their drink."""
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
        """Allows users the option to include an Add On in their drink."""
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
        """Allows the user to choose which type of tea they would like."""
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
        """Allows the user to choose which espresso drink they would like."""
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
        """Allows users to choose which type of drip coffee they would like."""
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
        """Allows users to choose which non-coffee option they want."""
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
        """Adds an item to a customer's order."""
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