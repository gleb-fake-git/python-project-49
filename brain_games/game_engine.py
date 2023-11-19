import prompt

GAME_SETTINGS = {
    'game_attempts': 3,
    'general_greetings': 'Welcome to the Brain Games!'
}


def welcome_user():
    """
    User greetings

    :return:
    """

    print(GAME_SETTINGS['general_greetings'])
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


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


def start_game(game_task: callable, rules: str):
    """
    Start game in depends what script was run

    :param game_task:
    :param rules:
    :return:
    """

    user_name = welcome_user()
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
