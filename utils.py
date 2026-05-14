import json
import random
from datetime import datetime

def generate_random_id(prefix="item"):
    unique_id = f"{prefix}_{random.randint(1000, 9999)}"
    return unique_id


def format_gaming_data(player_id, score, game_name):
    data = {
        "playerId": player_id,
        "score": score,
        "game": game_name,
        "timestamp": datetime.now().isoformat(),
        "id": generate_random_id("scoreboard")
    }
    return json.dumps(data)


def leaderboard_sort(gaming_data):
    leaderboard = sorted(gaming_data, key=lambda x: x['score'], reverse=True)
    return leaderboard


def filter_top_scores(gaming_data, top_n=10):
    leaderboard = leaderboard_sort(gaming_data)
    return leaderboard[:top_n]
