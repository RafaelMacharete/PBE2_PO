import random

class GuessingGame():
    def __init__(self): 
        self.random_num = random.randint(0, 10)

    def guess(self, guessed_num):
        if guessed_num == self.random_num:
            print('You are right')
            return False
        elif guessed_num > self.random_num:
            print('The number is smaller')
            return True
        else:
            print('The number is greater')
            return True 
    
guessing_game1 = GuessingGame()

continue_game = True

while continue_game:
    guessed_num = int(input("Guess a number between 0 and 10: "))
    continue_game = guessing_game1.guess(guessed_num)
