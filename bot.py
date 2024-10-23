from player import Player
import sys
import time
from termcolor import colored


class Bot3435(Player):
    def move(self):
        time.sleep(1)
        print("Bot's turn.")
        for letter in "Bot is calculating his move ...":
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.1)
        print(colored("\n\nBot has moved. Your turn!", "blue"))