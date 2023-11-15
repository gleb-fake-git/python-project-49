from random import randint
from brain_games.game_engine import welcome_user, get_user_answer, message_lose
from brain_games.game_engine import GAME_SETTINGS


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
    return right_answer, ' '.join(text_answer)


def main():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    attempts = GAME_SETTINGS['game_attempts']
    while attempts > 0:
        right_answer, text_answer = generate_task()
        print(f'Question: {text_answer}')
        user_message = int(get_user_answer())
        if user_message == right_answer:
            print('Correct!')
        else:
            message_lose(right_answer, user_message, user_name)
            break
        attempts -= 1
        if attempts == 0:
            print(f'Congratulations, {user_name}!')
            break


if __name__ == '__main__':
    main()
