from datastructures.deque import Deque
from projects.project3.program import Drink, Snack
import sys


class BistroSystem:
    """""Defines the system with which the bistro uses to run."""
    def __init__(self):
        """Defines the methods and items that the Bistro System uses."""
        from projects.project3.customerorder import CustomerOrder
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
        """Prompts the user to log in as a barista."""
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
        """Brings the user to the homescreen."""
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
        """Prints the selected menu for the user to view."""
        for category, items in menu.items():
            print(category)
            for item in items:
                print(f"  - {item}")
            print()

    def display_menu(self):
        """Allows the user to select which menu they want to view."""
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
        """Marks an order as complete and removes it from the Open Orders Deque."""
        ordercompleted = self.orders.dequeue()
        print(f"Order Up for {ordercompleted.name}!")
        for item in ordercompleted.items:
            if type(item) == Snack: print(item.name)
            elif type(item) == Drink: print(item.drinkstr)
        self.homescreen()

    def print_numbered_menu(self, menu):
        """Prints a numbered menu for options in a certain menu, used for building drinks."""
        for category, items in menu.items():
            print(category)
            for index, item in enumerate(items, start=1):
                print(f"  {index}. {item}")
            print()

    def begin_order(self):
        """Creates a new CustomerOrder with the desired name."""
        from projects.project3.customerorder import CustomerOrder
        ordername = input("What name would you like to use for your order? ")
        print(" ")
        neworder = CustomerOrder(ordername, self)
        neworder.order_items()

    def view_orders(self):
        """Views the Open Orders Deque and displays each order and its contents."""
        from projects.project3.customerorder import CustomerOrder
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
        """Displays the End of Day Report, including each item and order, as well as the total daily revenue."""
        from projects.project3.customerorder import CustomerOrder
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