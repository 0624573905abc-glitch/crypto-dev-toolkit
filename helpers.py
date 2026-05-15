import random
import string


def generate_random_string(length=12):
    """Generate a random string of fixed length.
    :param length: Length of the string to generate.
    :return: Randomly generated string.
    """  
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def calculate_win_probability(player_skill, opponent_skill):
    """Calculate win probability based on skill levels.
    :param player_skill: Skill level of the player (1-100).
    :param opponent_skill: Skill level of the opponent (1-100).
    :return: Win probability as a float between 0 and 1.
    """  
    total_skill = player_skill + opponent_skill
    return player_skill / total_skill if total_skill > 0 else 0.5


def format_currency(amount, currency_symbol='$'):
    """Format a float amount as currency.
    :param amount: The float amount to format.
    :param currency_symbol: The symbol for the currency.
    :return: Formatted currency string.
    """  
    return f'{currency_symbol}{amount:,.2f}'


def shuffle_list(items):
    """Shuffle a list in place.
    :param items: List of items to shuffle.
    """  
    random.shuffle(items)