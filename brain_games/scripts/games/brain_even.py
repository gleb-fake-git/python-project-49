from random import randint
from brain_games.game_engine import start_game


def generate_task() -> (str, int):
    """
    Generate random number and answer

    :return:
    """

    number = randint(1, 1000)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return right_answer, number


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(generate_task, rules)


if __name__ == '__main__':
    main()
