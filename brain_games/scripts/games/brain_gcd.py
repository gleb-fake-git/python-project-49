from random import randint
from brain_games.game_engine import welcome_user, get_user_answer, message_lose
from brain_games.game_engine import GAME_SETTINGS


def generate_task():
    a = randint(1, 100)
    b = randint(1, 100)
    text_answer = f'{a} {b}'
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b, text_answer


def main():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
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
