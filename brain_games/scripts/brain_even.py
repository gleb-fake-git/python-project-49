from random import randint
import prompt


def generate_task():
    number = randint(1, 1000)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return number, right_answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts = 3
    while attempts > 0:
        number, right_answer = generate_task()
        print(f'Question: {number}')
        user_message = prompt.string('')
        if user_message == right_answer:
            print('Correct!')
        else:
            message_lose(right_answer, user_message, name)
            break
        attempts -= 1
        if attempts == 0:
            print(f'Congratulations, {name}!')
            break


def message_lose(right, fail, name):
    print(f'\'{fail}\' is wrong answer ;(. Correct answer was \'{right}\'.')
    print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
