'''
Exercise: Hello World!

This script prints the classic "Hello, World!" and it greets the user by
name by printing "Hello, [user]!" where [user] is the input provided by the
user.

Usage:
    Run the script and follow the prompts to enter your name.

Tags: Python basics, print(), input()
'''


def main():
    '''Greet the world and the user.'''
    hello_world()
    user_name = input('Enter your name: ')
    hello_user(user_name)


def hello_world():
    '''Print a generic greeting to the world.'''
    print('Hello, World!')


def hello_user(username):
    '''
    Greet the user by name.

    Parameters:
        username (str): The name of the user

    Returns:
        None
    '''
    print(f'Hello, {username}!')


if __name__ == '__main__':
    main()
