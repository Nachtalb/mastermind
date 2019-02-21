# Simple Mastermind CLI game made with python

__author__ = 'Nachtalb'
__version__ = '1.0.1'
__date__ = '2019-02-21'

from collections import namedtuple
from random import choices

Pin = namedtuple('Pin', ('char', 'index', 'match_index'))


class MasterMind:
    available_chars = ['a', 'b', 'c', 'd', 'e']

    def __init__(self):
        self.answer = choices(self.available_chars, k=4)
        self.max_guesses = 10

    def start(self):
        print(f'Starting MasterMind\n'
              f'Available colour choices are: {", ".join(self.available_chars)}\n'
              f'Always guess 4 colors not more not less\n'
              f'{"-" * 40}')

        guess_counter = 0
        while True:
            guess_counter += 1
            guess = input(f'[{guess_counter}] Guess the code: ')
            if not guess or len(guess) != 4 or set(guess) - set(self.available_chars):
                continue

            positional_pins = self.get_positional_pins(guess)
            not_positional_pins = self.get_not_possitional_pins(guess, positional_pins)

            print(f'Positional correct: {len(positional_pins)}, not positional correct: {len(not_positional_pins)}')

            if list(guess) == self.answer:
                print('You won')
                break
            if guess_counter == self.max_guesses:
                print('You lost')
                break

    def get_positional_pins(self, guess):
        pins = []
        for index, char in enumerate(guess):
            if char == self.answer[index]:
                pins.append(Pin(char, index, index))
        return pins

    def get_not_possitional_pins(self, guess, blacklist_pins):
        pins = []
        for index, char in enumerate(guess):
            indexes_in_answer = [i for i, item in enumerate(self.answer) if item == char]
            if not indexes_in_answer:
                continue
            blacklist_indexes = [p.match_index for p in blacklist_pins]
            blacklist_indexes.extend([p.match_index for p in pins])

            white_list_indexes = set(indexes_in_answer) - set(blacklist_indexes)

            if index not in blacklist_pins and white_list_indexes:
                pins.append(Pin(index, char, list(white_list_indexes)[0]))
        return pins


if __name__ == '__main__':
    game = MasterMind()
    try:
        game.start()
    except KeyboardInterrupt:
        print('Exit')
