from random import randint
from brain_games.game_engine import start_game


def generate_task():
    a = randint(1, 100)
    b = randint(1, 100)
    text_answer = f'{a} {b}'
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return str(b), text_answer


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    start_game(generate_task, rules)


if __name__ == '__main__':
    main()
