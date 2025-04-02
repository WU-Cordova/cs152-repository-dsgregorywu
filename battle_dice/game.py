from character_type import CharacterType
import random
from character import Character

my_character_type = CharacterType.WARRIOR

class Game:
    """Manages the Dice Battle game logic."""
    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt."""
        attack_int = random.randint(1,6)
        power = attack_int * attacker.attack_power
        defender.health -= power
        printstr = str(attacker)
        printstr += "'s attack dealt "
        printstr += str(power)
        printstr += " damage."

    def start_battle(self):
        """Starts a turn-based battle between two players."""
        print("Battle started!")
        while self.__player1.health != 0 and self.__player2.health != 0:
            self.attack(self.__player1, self.__player2)
            self.attack(self.__player2, self.__player1)