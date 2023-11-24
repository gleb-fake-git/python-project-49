import prompt
from collections.abc import Callable
from typing import Union, Tuple


GAME_SETTINGS = {
    'game_attempts': 3,
    'general_greetings': 'Welcome to the Brain Games!'
}


def message_lose(right_answer: str, fail_answer: str, user_name: str):
    """
    Print loose message with right answer if user fail game

    :param right_answer:
    :param fail_answer:
    :param user_name:
    :return:
    """

    print(f'\'{fail_answer}\' is wrong answer ;(. Correct answer'
          f' was \'{right_answer}\'.')
    print(f'Let\'s try again, {user_name}!')


def start_game(game_task: Callable[[], Union[Tuple[str, int], Tuple[str, str]]], rules: str):
    """
    Start game in depends what script was run

    :param game_task:
    :param rules:
    :return:
    """

    print(GAME_SETTINGS['general_greetings'])
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(rules)
    attempts = GAME_SETTINGS['game_attempts']
    while attempts > 0:
        right_answer, text_answer = game_task()
        print(f'Question: {text_answer}')
        user_message = prompt.string('')
        if user_message == right_answer:
            print('Correct!')
        else:
            message_lose(right_answer, user_message, user_name)
            break
        attempts -= 1
        if attempts == 0:
            print(f'Congratulations, {user_name}!')
            break
