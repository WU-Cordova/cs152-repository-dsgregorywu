import sys
from datastructures.liststack import ListStack
from datastructures.deque import Deque
from projects.project3.program import BistroSystem
from projects.project3.customerorder import CustomerOrder

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
        if self.temp:
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
            if self.milk:
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