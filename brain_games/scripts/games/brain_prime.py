from random import randint
from brain_games.game_engine import start_game
from typing import Tuple


def generate_task() -> Tuple[str, str]:
    """
    Generate random number and answer

    :return:
    """

    number = randint(1, 1000)
    count_divided = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count_divided += 1
    right_answer = 'yes' if count_divided == 2 else 'no'
    return right_answer, number


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_game(generate_task, rules)


if __name__ == '__main__':
    main()
