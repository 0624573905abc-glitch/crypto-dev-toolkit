from typing import List, Dict, Any


def calculate_scores(player_stats: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate average score for each player based on their stats.
    
    Args:
        player_stats (List[Dict[str, Any]]): A list of dictionaries containing player statistics.
        Each dictionary must have 'name' and 'score' keys.

    Returns:
        Dict[str, float]: A dictionary with player names as keys and their average scores as values.
    """
    score_totals: Dict[str, float] = {}
    score_counts: Dict[str, int] = {}

    for stat in player_stats:
        name = stat['name']
        score = stat['score']
        if name in score_totals:
            score_totals[name] += score
            score_counts[name] += 1
        else:
            score_totals[name] = score
            score_counts[name] = 1

    average_scores = {name: total / score_counts[name] for name, total in score_totals.items()}
    return average_scores


def filter_top_players(scores: Dict[str, float], threshold: float) -> List[str]:
    """
    Filter the players who have an average score above a given threshold.
    
    Args:
        scores (Dict[str, float]): A dictionary with player names and their average scores.
        threshold (float): The score threshold for filtering players.

    Returns:
        List[str]: A list of player names who exceed the score threshold.
    """
    return [player for player, score in scores.items() if score > threshold]