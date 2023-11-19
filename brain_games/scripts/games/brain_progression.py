from random import randint
from brain_games.game_engine import start_game


def generate_task() -> (str, str):
    """
    Generate random progression and hidden number

    :return:
    """

    step = randint(2, 15)
    len_progression = randint(5, 10)
    number = randint(1, 50)
    stop = (((len_progression * step) + number) - step) + 1
    progression = list(map(str, range(number, stop, step)))
    hide_index = randint(0, len(progression) - 1)
    progression[hide_index], right_answer = '..', str(progression[hide_index])
    return str(right_answer), ' '.join(progression)


def main():
    rules = 'What number is missing in the progression?'
    start_game(generate_task, rules)


if __name__ == '__main__':
    main()
