import json
import random
from typing import List, Dict, Any

def generate_game_data(game_id: str, player_count: int) -> Dict[str, Any]:
    return {
        'game_id': game_id,
        'players': [generate_player_data(i) for i in range(1, player_count + 1)],
        'winner': get_random_winner(player_count)
    }


def generate_player_data(player_number: int) -> Dict[str, Any]:
    return {
        'player_id': f'player_{player_number}',
        'score': random.randint(0, 100),
        'level': random.choice([1, 2, 3, 4, 5])
    }


def get_random_winner(player_count: int) -> str:
    winner_index = random.randint(0, player_count - 1)
    return f'player_{winner_index + 1}'


def save_game_data_to_json(game_data: Dict[str, Any], filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(game_data, f, indent=4)


def load_game_data_from_json(filename: str) -> Dict[str, Any]:
    with open(filename, 'r') as f:
        return json.load(f)
