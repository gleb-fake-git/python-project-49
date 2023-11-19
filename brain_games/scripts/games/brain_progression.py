from random import randint
from brain_games.game_engine import start_game


def generate_task():
    step = randint(2, 15)
    len_progression = randint(5, 10)
    hidden_index = randint(0, len_progression - 1)
    number = randint(1, 50)
    right_answer = 0
    text_answer = []
    progression = []
    while len_progression != 0:
        progression.append(number)
        number += step
        len_progression -= 1
    for index, value in enumerate(progression):
        if index == hidden_index:
            text_answer.append('..')
            right_answer = value
        else:
            text_answer.append(str(value))
    return str(right_answer), ' '.join(text_answer)


def main():
    rules = 'What number is missing in the progression?'
    start_game(generate_task, rules)


if __name__ == '__main__':
    main()
