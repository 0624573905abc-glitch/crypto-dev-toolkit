import json
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

class GameHandler:
    def __init__(self):
        self.games = defaultdict(dict)

    def add_game(self, game_id, game_info):
        if game_id in self.games:
            logger.warning(f"Game with id {game_id} already exists. Updating info.")
        self.games[game_id].update(game_info)
        logger.info(f"Added/Updated game {game_id}")

    def get_game(self, game_id):
        game = self.games.get(game_id)
        if not game:
            logger.error(f"Game with id {game_id} not found.")
            return None
        return json.dumps(game)

    def remove_game(self, game_id):
        if game_id in self.games:
            del self.games[game_id]
            logger.info(f"Removed game {game_id}")
        else:
            logger.error(f"Game with id {game_id} does not exist.")

    def list_games(self):
        return json.dumps(self.games)

    def clear_games(self):
        self.games.clear()
        logger.info("Cleared all games")
