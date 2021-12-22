import random
cardValues = {"2": 2,
                  "3": 3,
                  "4": 4,
                  "5": 5,
                  "6": 6,
                  "7": 7,
                  "8": 8,
                  "9": 9,
                  "10": 10,
                  "Jack": 10,
                  "Queen": 10,
                  "King": 10,
                  "Ace": 11}
class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return f"{self.value} of {self.type}"

    types = ["hearts", "diamonds", "spades", "clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Deck():
    def __init__(self):
        self.deck = []
        for i in Card.types:
            for j in Card.values:
                self.deck.append(Card(i, j))
    def __str__(self):
        cards = ""
        for card in self.deck:
            cards = cards+f"{card}\n"
        return cards
    def __getitem__(self, index):
        return self.deck[index]
    def shuffle(self):
        random.shuffle(self.deck)


class Bet:
    def __init__(self, chips):
        self.chips = chips
    def place(self, amount):
        if self.chips>=amount:
            self.chips = self.chips-amount
        else:
            print("Not enough chips")

class Hand:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.result=cardValues[self.card1.value]+cardValues[self.card2.value]
    def stand(self):
        self.result = cardValues[self.card1.value]+cardValues[self.card2.value]
    def hit(self, card):
        self.result  = self.result+cardValues[card.value]
    def split(self):
        pass

class Dealer:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.result = cardValues[self.card1.value]+cardValues[self.card2.value]
class Game:
    chips = Bet(int(input("how may chips you want to buy: ")))
    prompt = "Y"
    while prompt.upper()=="Y":
        bet = int(input("how much do you want to bet: "))
        chips.place(bet)
        all_cards = Deck()
        all_cards.shuffle()
        print("DEALERS CARDS")
        deal = Dealer(all_cards.deck.pop(0), all_cards.deck.pop(0))
        print(f"{deal.card1}\n")
        print("PLAYERS CARDS")
        hand = Hand(all_cards.deck.pop(0), all_cards.deck.pop(0))
        print(hand.card1)
        print(hand.card2)
        decision = input("do you wish to stand, hit, double: ")
        while hand.result < 21 and decision.lower() != "stand":
            if decision.lower() == "hit":
                hand.hit(all_cards.deck.pop(0))
                print(all_cards.deck.pop(0))
                if hand.result <= 21:
                    decision = input("do you wish to stand, hit, double: ")
            elif decision.lower() == "stand":
                result = hand.result
            elif decision.lower() == "double":
                chips.chips = chips.chips * 2
                chips = chips - bet
                decision = input("do you wish to stand, hit, double: ")
            else:
                print("Invalid operation. Try Again")
                decision = input("do you wish to stand, hit, double: ")
        print(f"THE DEALERS OTHER CARD: {deal.card2} ")
        if hand.card1.value=="Ace" or hand.card2.value=="Ace" and hand.result>21:
            cardValues["Ace"]=1
        else:
            cardValues["Ace"]=11
        if hand.result > 21:
            print(f"You lose. You went over 21. Your result: {hand.result}")
            print(f"You have {chips.chips} left")
            prompt = input("Do you wish to play again Y/N: ")
        elif hand.result < deal.result:
            print(f"You lose. You didn't beat the dealer. Your result: {hand.result}. Dealers result: {deal.result}")
            print(f"You have {chips.chips} left")
            prompt = input("Do you wish to play again Y/N: ")
        elif hand.result > deal.result:
            print("You win.")
            prompt = input("Do you wish to play again Y/N: ")
            chips.chips=chips.chips+bet*3
            print(f"You have {chips.chips} left")
        elif hand.result==deal.result:
            print("A Tie")