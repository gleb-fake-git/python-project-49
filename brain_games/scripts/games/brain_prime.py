from random import randint
from brain_games.game_engine import welcome_user, get_user_answer, message_lose
from brain_games.game_engine import GAME_SETTINGS


def generate_task():
    number = randint(1, 1000)
    count_divided = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count_divided += 1
    right_answer = 'yes' if count_divided == 2 else 'no'
    return number, right_answer


def main():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    attempts = GAME_SETTINGS['game_attempts']
    while attempts > 0:
        number, right_answer = generate_task()
        print(f'Question: {number}')
        user_message = get_user_answer()
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
