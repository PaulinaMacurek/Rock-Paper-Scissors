import random
import math


class Person:
    def __init__(self):
        self.name = input('Enter your name: ')
        self.greeting()
        self.score = self.read_scores()
        self.options = self.read_options()

    def __str__(self):
        return f'Name : {self.name} \nScore: {self.score}'

    def greeting(self):
        print(f'Hello, {self.name}')

    def add_score(self, score_):
        self.score += score_

    def read_scores(self):
        with open("rating.txt", 'w+',  encoding='utf-8') as file:
            for line in file:
                if self.name == line.split()[0]:
                    score = line.split()
                    return int(score[1])
        return 0

    @staticmethod
    def read_options():
        read = input()
        if read != '':
            return read.split(',')
        else:
            return ['rock', 'paper', 'scissors']


class RockPaperScissors:

    def __init__(self, rating, options_provided):
        self.actual_rating = rating
        self.options_provided = options_provided
        self.user_option = self.check_input()
        self.computer_option = random.choice(options_provided)

    def __str__(self):
        return f"A playable Rock-Paper-Scissors game, with a Player vs Computer mode."

    def game_result(self):
        opt_len = len(self.options_provided)
        user_index = self.options_provided.index(self.user_option)
        computer_index = self.options_provided.index(self.computer_option)
        indexes_beaten_by_user = [((user_index + i) % opt_len) for i in range(1, math.ceil(opt_len / 2))]
        if computer_index == user_index:
            print(f"There is a draw ({self.computer_option})")
            return 50
        elif computer_index in indexes_beaten_by_user:
            print(f"Sorry, but the computer chose {self.computer_option}")
            return 0
        else:
            print(f"Well done. The computer chose {self.computer_option} and failed")
            return 100

    def check_input(self):
        while True:
            option = input()

            if option in self.options_provided:
                return option
            elif option == "!exit":
                self.exit()
            elif option == '!rating':
                print(f"Your rating: {self.actual_rating}")
            else:
                print("Invalid input")

    @staticmethod
    def exit():
        print("Bye!")
        exit()


def main():

    paulina = Person()
    print("Okay, let's start")

    while True:
        game = RockPaperScissors(paulina.score, paulina.options)
        paulina.add_score(game.game_result())


if __name__ == "__main__":
    main()
