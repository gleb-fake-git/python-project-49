from random import randint, choice
from brain_games.game_engine import welcome_user, get_user_answer, message_lose
from brain_games.game_engine import GAME_SETTINGS


def generate_task():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operations = ['+', '-', '*']
    operation = choice(operations)
    answer_text = f'{number1} {operation} {number2}'
    if operation == '+':
        answer_number = number1 + number2
    elif operation == '-':
        answer_number = number1 - number2
    else:
        answer_number = number1 * number2

    return answer_number, answer_text


def main():
    user_name = welcome_user()
    print('What is the result of the expression?')
    attempts = GAME_SETTINGS['game_attempts']
    while attempts > 0:
        right_answer, answer_text = generate_task()
        print(f'Question: {answer_text}')
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
