import prompt

GAME_SETTINGS = {
    'game_attempts': 3,
    'general_greetings': 'Welcome to the Brain Games!'
}


def welcome_user():
    print(GAME_SETTINGS['general_greetings'])
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    user_answer = prompt.string('')
    return user_answer


def message_lose(right_answer, fail_answer, user_name):
    print(f'\'{fail_answer}\' is wrong answer ;(. Correct answer was \'{right_answer}\'.')
    print(f'Let\'s try again, {user_name}!')
