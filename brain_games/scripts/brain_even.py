from brain_games.scripts.cli_utils import greet_user, get_string_from_user
from brain_games.scripts.even_game import play_even_game


def main():
    greet_user()
    print('Answer "yes" if number even otherwise answer "no".\n')

    user_name = get_string_from_user('May I have your name? ')
    print(f'Hello, {user_name}!\n')
    result = play_even_game()

    if result:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    main()
