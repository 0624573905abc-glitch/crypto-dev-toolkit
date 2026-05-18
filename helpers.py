from typing import List, Dict, Any


def calculate_reward(level: int, performance: float) -> float:
    """Calculate the reward based on level and performance.

    Args:
        level (int): The player level.
        performance (float): The performance score (0 to 1).

    Returns:
        float: The calculated reward.
    """
    base_reward = 100.0
    modifier = 1 + (level * 0.1)
    return base_reward * modifier * performance


def format_player_data(player_data: Dict[str, Any]) -> str:
    """Format player data into a readable string.

    Args:
        player_data (Dict[str, Any]): A dictionary containing player data.

    Returns:
        str: A formatted string of player data.
    """
    return f"Player {player_data['name']} (Level: {player_data['level']}) - Score: {player_data['score']:.2f}"


def filter_high_scorers(players: List[Dict[str, Any]], threshold: float) -> List[Dict[str, Any]]:
    """Filter players based on their scores being above a threshold.

    Args:
        players (List[Dict[str, Any]]): A list of player dictionaries.
        threshold (float): The minimum score to qualify.

    Returns:
        List[Dict[str, Any]]: A list of qualifying player dictionaries.
    """
    return [player for player in players if player['score'] > threshold]
