import random
import time

class CardGame:
    def __init__(self, players_list):
        self.players_list = players_list
        self.cards = self.create_cards()
        self.hand = {player: [] for player in players_list}

    def create_cards(self):
        colors_list = ['Vermelho', 'Azul', 'Verde', 'Amarelo']
        valores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+2', 'Inverter', 'Pular']
        cards = []
        for color in colors_list:
            for value in valores:
                cards.append(f"{value} {color}")
        return cards * 2

    def embaralhar_cartas(self):
        random.shuffle(self.cards)

    def throw_cards(self, num_cards=7):
        for player in self.players_list:
            cards = []
            for _ in range(num_cards):
                if self.cards:
                    cards.append(self.cards.pop())
            self.hand[player] = cards

    def play(self, player, card):
        if card in self.hand[player]:
            self.hand[player].remove(card)
            print(f"{player} jogou {card}!")
        else:
            print(f"{player} não tem a carta {card}.")

players_list = ["Alice", "Bob", "Carol"]
game = CardGame(players_list)

game.embaralhar_cartas()
game.throw_cards()
print(game.hand)

time.sleep(3)

game.play("Alice", game.hand["Alice"][0])
game.play("Alice", '3 Azul')
print(game.hand)