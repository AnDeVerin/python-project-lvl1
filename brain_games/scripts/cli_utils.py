import prompt


def greet_user():
    """Greet the user."""
    print('Welcome to the Brain Games!')


def get_string_from_user(question):
    """Ask user to answer question"""
    return prompt.string(question)
