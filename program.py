from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from datastructures.bag import Bag
from random import shuffle, choice

# Constants - Defines the structure of a deck
decks = [2, 4, 6, 8]
cards = {"A": 11, "2": "2", "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
suits = ["♡", "♢", "♧", "♤"]
deck = Bag()

class Blackjack():

    def __init__(self):
        print("")
        print("Welcome to Blackjack!")
        self._balance = int(0)
        self._allcards = {}
        self._dealer_hand = []
        self._player_hand = []
        self._player_score = 0
        self._dealer_score = 0
        self._busted = False
        self._dbusted = False
        self._player_aces = int(0)
        self._dealer_aces = int(0)
        self._wager = int(0)

    def assort_cards(self):
        """Creates a deck of cards and adds them to the deck, once for each deck included."""
        deck.clear()
        for i in range(self._decks):
            for suit in suits:
                for card, value in cards.items():
                    cardnumber = f"{card}{suit}"  
                    deck.add(cardnumber)
                    self._allcards[cardnumber] = cards[card] 
        
    def shuffle_deck(self):
        """Shuffles remaining cards in deck."""
        shuffle(deck._contents)  

    def deal_cards(self):
        """Deals cards to the player and dealer."""
        for i in range(2):
            card = deck._contents[0]
            self._dealer_hand.append(card)
            deck.remove(card)
        for i in range(2):
            card = deck._contents[0]
            self._player_hand.append(card)
            deck.remove(card)
        for card in self._player_hand:
            self._player_score += int(self._allcards[card])
        for card in self._dealer_hand:
            self._dealer_score += int(self._allcards[card])
        self._player_aces = sum(1 for card in self._player_hand if self._allcards[card] == 11)
        self._dealer_aces = sum(1 for card in self._dealer_hand if self._allcards[card] == 11)
        

    def play_again(self):
        """Asks the user if they want to play again."""
        while True:
            response = input("Would you like to play again? (Y)es or (N)o: ").strip().upper()
            if response == "Y":
                self.main()
                break
            elif response == "N":
                print("Game over! Thanks for playing!")
                exit()
            else:
                print("Invalid response. Please type 'Y' to play again or 'N' to quit.")
        
    def hit(self):
        """The player decides to hit and get another card."""
        print("")
        print("You chose to hit.")
        card = deck._contents[0]
        self._player_hand.append(card)
        deck.remove(card)
        self._player_score += int(cards[card[:-1]])
        drewstr = str("You drew [")
        drewstr += str(card)
        drewstr += "]"
        print(drewstr)
        print("")
        if self._allcards[card] == 11:
            self._player_aces += 1
        self.adjust_for_aces()
        if self._player_score > 21:
            self._busted = True
            self.compare_scores()
        elif self._player_score == 21:
            print("You got 21!")
            print("")
            self.reveal_dealer()

    def stay(self):
        """The player decides to stay."""
        print("")
        print("You chose to stay.")
        self.reveal_dealer()

    def adjust_for_aces(self):
        """Adjusts the score for aces if the score is above 21."""
        while self._player_score > 21 and self._player_aces > 0:
            self._player_score -= 10
            self._player_aces -= 1
        while self._dealer_score > 21 and self._dealer_aces > 0:
            self._dealer_score -= 10
            self._dealer_aces -= 1
    
    def place_wager(self):
        looping = True
        while looping == True:
            response = input("Please enter an amount to wager. $").strip().upper()
            digits = response.isdigit()
            if digits == True:
                self._wager = int(response)
                self._balance -= self._wager
                looping = False 
            else: print("Please enter a valid number. ")
        wagerstr = str(self._wager).strip()
        print("You wagered $" + wagerstr + ".")
        print("")

    def reveal_dealer(self):
        """Reveals the dealer's hand."""
        dealerhandstr = f"Dealer's Hand: [{self._dealer_hand[0]}] [{self._dealer_hand[1]}] | Score: {self._dealer_score}"
        print(dealerhandstr)
        print("")
        while self._dealer_score < 17:
            self.dealer_hit()
            print(f"Dealer Score: {self._dealer_score}")
            print("")
        if self._dealer_score > 21:
            self._dbusted = True
        self.compare_scores()
            
    def dealer_hit(self):
        """Dealer draws a card."""
        card = deck._contents[0]
        self._dealer_hand.append(card)
        deck.remove(card)
        temp_score = self._dealer_score
        temp_score += int(self._allcards[card])
        if temp_score > 21 and self._dealer_aces > 1:
            self._dealer_score -= 10
            self._dealer_aces -= 1
        self._dealer_score += int(self._allcards[card])
        if self._allcards[card] == 11:
            self._dealer_aces += 1
        self.adjust_for_aces()
        print("Dealer drew", str(card))

    def compare_scores(self):
        """Compares the player's and dealer's scores and ends the game."""
        if self._busted == True:
            print("You busted! The dealer wins.")
        elif self._dbusted == True:
            print("The dealer busted. You win!")
            self._balance += int(self._wager * 2)
        elif self._player_score == 21 and not self._dealer_score == 21 and self._player_blackjack == True:
            print("Blackjack! You win!")
            self._balance += int(self._wager + self._wager * 1.5)
        elif self._dealer_hand == 21 and not self._player_score == 21:
            print("Dealer blackjack! You lose.")
        elif self._player_score < self._dealer_score:
            print(f"You lose! Player score: {self._player_score}, Dealer score: {self._dealer_score}")
        elif self._player_score == self._dealer_score:
            print(f"It's a tie! Player score: {self._player_score}, Dealer score: {self._dealer_score}")
            self._balance += self._wager
        elif self._player_score > self._dealer_score:
            print(f"You win! Player score: {self._player_score}, Dealer score: {self._dealer_score}")
            self._balance += int(self._wager * 2)
        if self._balance < 0:
            print("Current Balance: -$" + str(abs(self._balance)))
        else: print("Current Balance: $" + str(self._balance))
        print("")
        self.play_again()

    def main(self):
        """Runs one game of blackjack."""
        deck.clear()
        self._decks = choice(decks)
        self._player_blackjack = False
        self._player_score = int(0)
        self._dealer_score = int(0)
        self._busted = False
        self._dbusted = False
        self._player_hand = []
        self._dealer_hand = []
        self._player_aces = int(0)
        self._dealer_aces = int(0)
        self.assort_cards()
        self.shuffle_deck()
        self.deal_cards()
        print("")
        self.place_wager()
        print("Initial Deal:")
        print("")
        playerhandstr = f"Player's Hand: [{self._player_hand[0]}] [{self._player_hand[1]}] | Score: {self._player_score}"
        if self._dealer_score != 21:
            dealerhandstr = f"Dealer's Hand: [{self._dealer_hand[0]}] [Hidden] | Score: {cards[self._dealer_hand[0][:-1]]}"
        else:
            dealerhandstr = f"Dealer's Hand: [{self._dealer_hand[0]}] [{self._dealer_hand[1]}] | Score: {self._dealer_score}"
        print(playerhandstr)
        print(dealerhandstr)
        print("")
        if self._player_score == 21:
            self._player_blackjack = True
            self.compare_scores
        if self._dealer_score == 21:
            self.compare_scores()
        while not self._busted and self._player_score <= 21:
            response = input("Would you like to (H)it or (S)tay? ").strip().upper()
            if response == "H":
                self.hit()
                printstr = "Player's Hand: "
                for card in (self._player_hand):
                    printstr += '['
                    printstr += str(card) 
                    printstr += "] "
                printstr += "| Score: "
                printstr += str(self._player_score)
                print(printstr)
            elif response == "S":
                self.stay()
                break
            else:
                print("Invalid response. Please type 'H' to Hit or 'S' to Stay.")

if __name__ == "__main__":
    game = Blackjack()
    game.main()