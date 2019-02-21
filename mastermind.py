# Simple Mastermind CLI game made with python
__author__ = 'Nachtalb'
__version__ = '1.0.0'
__date__ = '2019-02-21'

from random import choices


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
        print(self.answer)

        guess_counter = 0
        while True:
            guess_counter += 1
            guess = input(f'[{guess_counter}] Guess the code: ')
            if not guess or len(guess) != 4 or set(guess) - set(self.available_chars):
                continue

            positional_correct = 0
            correct = 0
            for index, char in enumerate(guess):
                if char in self.answer and char == self.answer[index]:
                    positional_correct += 1
                elif char in self.answer:
                    correct += 1

            print(f'Positional correct: {positional_correct}, not positional correct: {correct}')

            if list(guess) == self.answer:
                print('You won')
                break
            if guess_counter == self.max_guesses:
                print('You lost')
                break


if __name__ == '__main__':
    game = MasterMind()
    try:
        game.start()
    except KeyboardInterrupt:
        print('Exit')
