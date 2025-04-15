import sys
#from datastructures.liststack import ListStack

class Drink:
    """A Drink ordered from the Bearcat Bistro."""
    def __init__(self, size):
        self.size = size
        self.cost = float

class Snack:
    """A snack ordered from the bistro."""
    def __init__(self, item):
        if item in self.snacks: self.item = item
        else: raise IndexError("Item not available.")
        self.cost = self.snacks[item]
        

class OrderItem:
    """A drink with a customization."""
    def __init__(self, message):
        self.message = str()

class CustomerOrder:
    """A customer's order, including name, price, and each item ordered"""
    def __init__(self, name):
        self.price = float
        self.items = []
        self.name = name

    def order_items(self):
        response = input("Would you like a (D)rink or (S)nack? ").strip().upper()
        print("    ")
        if response == "D":
            self.print_numbered_menu({"Bases": self.bases})
            drink_choice = input("Please select a base by number.").strip()
            if drink_choice.lower() == "quit":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif drink_choice.lower() == "b": 
                print("Exiting the menu.")
                self.homescreen()
            elif drink_choice.isdigit():
                index = int(drink_choice) - 1
                if 0 <= index < len(self.bases):
                    selected_base = list(self.bases.keys())[index]
                    print(f"You selected: {selected_base}")
                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid input. Please enter a number or type 'quit'.")
        elif response == "S":
            self.print_numbered_menu({"Snacks": self.snacks})
            snack_choice = input("Please select a snack by number or type 'quit' to exit: ").strip()
            if snack_choice.lower() == "quit":
                print("Exiting Bearcat Bistro.")
                sys.exit()
            elif snack_choice.isdigit():
                index = int(snack_choice) - 1
                if 0 <= index < len(self.snacks):
                    selected_snack = list(self.snacks.keys())[index]
                    print(f"You selected: {selected_snack}")
                    newsnack = Snack(selected_snack)
                    looping = True
                    while looping:
                        response = input(f"Would you like to add {selected_snack} to your order? (Y)es or (N)o?")
                        if response.lower() == "y": 
                            self.add_item(newsnack)
                            looping = False
                        elif response.lower() == "n":
                            looping = False
                        else: print("Invalid response. Please try again.")
                    self.homescreen()


                else:
                    print("Invalid selection. Please choose a valid number.")
            else:
                print("Invalid input. Please enter a number or type 'quit'.")
        else:
            print("Invalid selection. Please choose 'D' for Drink or 'S' for Snack.")

    def add_to_order(self, item):
        if not type(item) == Snack and not type(item) == Drink: raise TypeError("Item not of correct type.")
        self.items.append(item)
        self.price += item.cost


def main():
    
    print("Hello, World!")



if __name__ == '__main__':
    main()
