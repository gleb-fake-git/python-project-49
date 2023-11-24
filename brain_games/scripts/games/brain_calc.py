from random import randint, choice
from brain_games.game_engine import start_game
from typing import Tuple


def generate_task() -> Tuple[str, str]:
    """
    Generate random number and answer

    :return:
    """

    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operations = ['+', '-', '*']
    operation = choice(operations)
    answer_text = f'{number1} {operation} {number2}'
    calculation = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    answer_number = calculation[operation](number1, number2)

    return str(answer_number), answer_text


def main():
    rules = 'What is the result of the expression?'
    start_game(generate_task, rules)


if __name__ == '__main__':
    main()
