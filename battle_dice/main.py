from game import Game
from character import Character
from character_type import CharacterType

alice = Character(name = "Alice", character_type = CharacterType.WARRIOR, health = 100, attack_power = 10)
bob = Character(name = "Bob", character_type = CharacterType.MAGE, health = 70, attack_power = 15)


if __name__ == "__main__":
    game = Game(alice, bob)
    game.start_battle()